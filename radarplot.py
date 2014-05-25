import sys
d = []
for i in sys.path:
    if 'Tribon' in i:
        d.append(i)
for j in d:
    sys.path.remove(j)

import math
import random
import wx
class RadarGraph(wx.Window):
    def __init__(self, parent, title, labels):
        wx.Window.__init__(self, parent)
        self.title = title
        self.labels = labels
        self.data = [0.0] * len(labels)
        self.titleFont = wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.labelFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.InitBuffer()
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    def OnSize(self, evt):
        # When the window size changes we need a new buffer.
        self.InitBuffer()
    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self, self.buffer)
    def InitBuffer(self):
        w, h = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(w, h)
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc)
    def GetData(self):
        return self.data
    def SetData(self, newData):
        assert len(newData) == len(self.data)
        self.data = newData[:]
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc)
    def PolarToCartesian(self, radius, angle, cx, cy):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        return (cx+x, cy-y)
    def DrawGraph(self, dc):
        spacer = 10
        scaledmax = 150.0
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dw, dh = dc.GetSize()
        dc.SetFont(self.titleFont)
        tw, th = dc.GetTextExtent(self.title)
        dc.DrawText(self.title, (dw-tw)/2, spacer)
        th = th + 2*spacer
        cx = dw/2
        cy = (dh-th)/2 + th
        mindim = min(cx, (dh-th)/2)
        scale = mindim/scaledmax
        dc.SetPen(wx.Pen("black", 1))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawCircle(cx,cy, 25*scale)
        dc.DrawCircle(cx,cy, 50*scale)
        dc.DrawCircle(cx,cy, 75*scale)
        dc.DrawCircle(cx,cy, 100*scale)
        dc.SetPen(wx.Pen("black", 2))
        dc.DrawLine(cx-110*scale, cy, cx+110*scale, cy)
        dc.DrawLine(cx, cy-110*scale, cx, cy+110*scale)
        dc.SetFont(self.labelFont)
        maxval = 0
        angle = 0
        polypoints = []
        for i, label in enumerate(self.labels):
            val = self.data[i]
            point = self.PolarToCartesian(val*scale, angle, cx, cy)
            polypoints.append(point)
            x, y = self.PolarToCartesian(125*scale, angle, cx,cy)
            dc.DrawText(label, x, y)
            if val > maxval:
                maxval = val
            angle = angle + 360/len(self.labels)
            c = "forest green"
        if maxval > 70:
            c = "yellow"
        if maxval > 95:
            c = "red"
        dc.SetBrush(wx.Brush(c))
        dc.SetPen(wx.Pen("navy", 3))
        dc.DrawPolygon(polypoints)
class TestFrame(wx.Frame):
    def __init__(self):
            wx.Frame.__init__(self, None, title="Double Buffered Drawing",
                                size=(480,480))
            self.plot = RadarGraph(self, "Sample 'Radar' Plot",
                                ["A", "B", "C", "D", "E", "F", "G", "H"])
            # Set some random initial data values
            data = []
            for d in self.plot.GetData():
                data.append(random.randint(0, 75))
            self.plot.SetData(data)
            # Create a timer to update the data values
            self.Bind(wx.EVT_TIMER, self.OnTimeout)
            self.timer = wx.Timer(self)
            self.timer.Start(500)
    def OnTimeout(self, evt):
        # simulate the positive or negative growth of each data value
        data = []
        for d in self.plot.GetData():
            val = d + random.uniform(-5, 5)
            if val < 0:
                val = 0
            if val > 110:
                val = 110
            data.append(val)
        self.plot.SetData(data)
app = wx.PySimpleApp()
frm = TestFrame()
frm.Show()
app.MainLoop()