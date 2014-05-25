#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     28/02/2014
# Copyright:   (c) binoy.pilakkat 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx,os,re,shelve
import sys
d = []
for i in sys.path:
    if 'Tribon' in i:
        d.append(i)
for j in d:
    sys.path.remove(j)

from scheme import SchemeFile,Panel,Bound,AttrDisplay
import Materials,sys
dbpath=""
class TestListCtrl(wx.ListCtrl):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LC_REPORT):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
    def _AddColumn(self,_index,_head):
            wx.ListCtrl.InsertColumn(self,_index,_head,wx.LIST_FORMAT_CENTER)
        #wxListCtr#lAutoWidthMixin.__init__(self)
    def _AddRowdata(self,rno,text,col=None):
        return wx.ListCtrl.InsertStringItem(self,rno,text)
    def Dest(self):
        wx.ListCtrl.DeleteAllColumns(self)
class mainOut(wx.TextCtrl):
    def __init__(self,parent,Pos,Size):
        wx.TextCtrl.__init__(self,parent,pos=Pos,size =Size ,\
        style =wx.TE_MULTILINE)


class mainWindow(wx.Frame):
    """
    The main Frame of the application
    """

    def __init__(self,pl):
        """
        Initialize the main frame methods
        Structure of the mainWindow is defined here
        """
        _tit  = "PartList Checker"  #Title of main window
        _size = (700,800)           # size of main window
        _sty  = wx.DEFAULT_FRAME_STYLE^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        wx.Frame.__init__(self,None,-1,_tit,(-1,-1),_size,_sty)
        self.partlist = pl
        self._panel = wx.Panel(self)
        self._label1 = wx.StaticText(self._panel,id = -1,label = "Position No",\
        pos = (20,20),size = (80,-1))

        # Main text input
        self._txtPos = wx.TextCtrl(self._panel,id = -1,pos = (100,15),\
        size = (50,-1),style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.Check, self._txtPos)

        # ################################################
        #Check Button
        self._cmdCheck = wx.Button(self._panel,-1,pos=(20,55),label ="Check",\
        size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.Check,self._cmdCheck)

        # ################################################

        #Get Detail Button
        self._cmdGetinfo = wx.Button(self._panel,10,\
        pos=(130,55),label = "Show Partlist",size =(100,-1))
        # ################################################

        #Get Checked items Button
        self._cmdCheckedParts= wx.Button(self._panel,-1,\
        pos=(20,90),label = "Checked Parts",size=(100,-1))
        # ################################################

        #Get UnChecked items Button
        self._cmdUnCheckedParts= wx.Button(self._panel,-1,\
        pos=(130,90),label = "UnChecked Parts")
        # ################################################

        #Get Thickness Sort  Button
        self._cmdThickness= wx.Button(self._panel,-1,\
        pos=(350,90),label = "Calculate Running Length")
        # ################################################

        #Get Partinfo  Button
        self._cmdPartinfo= wx.Button(self._panel,-1,\
        pos=(160,15),label = "PartInfo")
        # ################################################
        #Details Display

        self.Display =  mainOut(self._panel,Pos=(350,130),Size = (300,300))

        #Message Display
        self.Messages =  mainOut(self._panel,Pos=(350,440),Size = (300,200))

        #List
        self.lstCtr = TestListCtrl(self._panel,ID=-1,pos= (20,130),\
        style = wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|wx.LC_SORT_ASCENDING,\
        size=(300,600))


        # event Bindings
        self.Bind(wx.EVT_BUTTON,self.LoadContentsToList,self._cmdGetinfo)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON,self._shwUnchecked,self._cmdUnCheckedParts)
        self.Bind(wx.EVT_BUTTON,self._shwchecked,self._cmdCheckedParts)
        self.Bind(wx.EVT_BUTTON,self._CalculateLength,self._cmdThickness)
        self.Bind(wx.EVT_BUTTON,self.partInfo,self._cmdPartinfo)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self._listact,self.lstCtr)

    def LoadContentsToList(self,event):
        self.lstCtr.Dest()
        """
        Function to fill up the list control
        """
##        print event.GetEventObject().GetId()
        self.lstCtr.DeleteAllItems()
        #Filling list control
        self.lstCtr._AddColumn(1,"Position")
        self.lstCtr._AddColumn(2,"Quantity")
        self.lstCtr._AddColumn(3,"ProfileShape")
        self.lstCtr._AddColumn(4,"Dimension")
        self.lstCtr._AddColumn(5,"Weight")
        self.lstCtr._AddColumn(6,"Length")
        indx=1
        for eachpart in self.partlist:
            c= self.lstCtr._AddRowdata(indx, eachpart[1].Position)
            self.lstCtr.SetStringItem(c,1,str(eachpart[1].Quantity))
            self.lstCtr.SetStringItem(c,2,str(eachpart[1].ProfileShape))
            self.lstCtr.SetStringItem(c,3,str(eachpart[1].Dimension))
            self.lstCtr.SetStringItem(c,4,str(eachpart[1].Weight))
            self.lstCtr.SetStringItem(c,5,str(eachpart[1].Length))
            indx +=1

    def Check(self,event):
        """
        Check the given pos no
        """
        self.Display.SetValue("")
        self.Messages.SetValue("")
        p = self._txtPos.GetValue()
        print p
        if "." in p:
            [p,n] = p.split(".")
            p = str(p)
            n = int(n)
            print [p,n]
            try:
                msg =  self.partlist.members[p].Count(n)
                self.getDetail(event)
            except:
                msg = "Check failed\n"+str(Exception.message)
        elif "-" in p:
            try:
                [s1,s2] = p.split("-")
                _cou = int(s2)-int(s1)
##                        print s1,s2,_cou
                for _p in range(_cou):
                    s1 = int(s1)
                    msg ="Checked" + str(s1)
                    self.partlist.members[str(s1)].Count()
                    s1 +=1
            except:
                msg = "Error in continuous counting"+str(Exception.message)
        else:
            p = p
            try:
                msg = self.partlist.members[p].Count()
                self.getDetail(event)
            except:
                msg = "Check failed"
        self.Messages.SetValue(msg)
        dbUpdate(self.partlist)
        self._txtPos.SetValue("")
        self._txtPos.SetFocus()

    def getDetail(self,event):
        self.Display.SetValue("")
        self.Messages.SetValue("")
        p = self._txtPos.GetValue()
        if "." in p:
            [p,n] = p.split(".")
            p = str(p)
            n = int(n)
        self.Display.SetValue(self.partlist[p])
    def _listact(self,event):
        p= event.GetItem()
        self._txtPos.SetValue(str(p.GetText()))
        self.partInfo(event)

    def partInfo(self,event):
        self.Display.SetValue("")
        self.Messages.SetValue("")

        p = self._txtPos.GetValue()
        if "." in p:
            [p,n] = p.split(".")
            p = str(p)
            n = int(n)
        info = self.partlist[p]


##        try:
##            _Lfl_ = self.partlist.members[p].Description.lower().split('-')
##            inpPan = '-'.join(_Lfl_[:-1])
##            curSch_ = SchemeFile(inpPan)
##            self.Messages.SetValue(unicode(curSch_.PanelDetails()))
##        except:
##            info +=     "\n\tScheme Error" + str(Exception.message)
##

        #info += curSch_.ExcesDetails()


        self.Display.SetValue(info)

    def OnCloseWindow(self, event):
        """
        While Exiting

        """
        dbUpdate(self.partlist)
        self.Destroy()
        wx.Exit()
##        self.sp.Initialize()
    def _funCmdCheck(self,event):
        """
        On check button click
        """
        print str(event)
        print self._txtPos.GetValue()
        print self._cmdUnCheckedParts.GetSizeTuple()

    def _shwUnchecked(self,event):
        self.lstCtr.Dest()
        txt = self.partlist.showUnchecked()
        self.lstCtr.DeleteAllItems()
        #Filling list control
        self.lstCtr._AddColumn(1,"Position")
        self.lstCtr._AddColumn(2,"Quantity Checked")
        self.lstCtr._AddColumn(3,"Quantity")

        indx=1
        for eachpart in txt:
            c= self.lstCtr._AddRowdata(indx, eachpart[0])
            self.lstCtr.SetStringItem(c,1,str(eachpart[1]))
            self.lstCtr.SetStringItem(c,2,str(eachpart[2]))

            indx +=1
    def _shwchecked(self,event):
##        txt = self.partlist.showChecked()
        self.lstCtr.Dest()
        txt = self.partlist.showChecked()
        self.lstCtr.DeleteAllItems()
        #Filling list control
        self.lstCtr._AddColumn(1,"Position")
        self.lstCtr._AddColumn(2,"Quantity Checked")
        self.lstCtr._AddColumn(3,"Quantity")

        indx=1
        for eachpart in txt:
            c= self.lstCtr._AddRowdata(indx, eachpart[0])
            self.lstCtr.SetStringItem(c,1,str(eachpart[1]))
            self.lstCtr.SetStringItem(c,2,str(eachpart[2]))
    def _thknessSort(self,event):
        self.lstCtr.Dest()
        DictThickness = {}

        for item in activePartlist:
            curKey=item[1].Thickness
            if curKey in DictThickness:
                DictThickness[curKey].append([item[1].Position,\
                item[1].ActCutName,item[1].Description])
            else:
                DictThickness[curKey]=[]
                DictThickness[curKey].append([item[1].Position,\
                item[1].ActCutName,item[1].Description])

            curKey =None
        dlg = wx.SingleChoiceDialog(None,
        'Plates',
        'Thickness sort',
        DictThickness.keys())

        if dlg.ShowModal() == wx.ID_OK:
            thk = dlg.GetStringSelection()

        # fill the lstctr
        self.lstCtr._AddColumn(1,"Position Number")
        self.lstCtr._AddColumn(2,"Plate name")
        self.lstCtr._AddColumn(3,"Description")
        self.lstCtr.SetColumnWidth(0, 100)
        self.lstCtr.SetColumnWidth(1, 200)
        self.lstCtr.DeleteAllItems()
        indx=1
        if thk in sorted(DictThickness.keys()):
            outList =sorted(DictThickness[thk])
            print outList
            for i in outList:
                c= self.lstCtr._AddRowdata(indx, i[0])
                self.lstCtr.SetStringItem(c,1,i[1])
                self.lstCtr.SetStringItem(c,2,i[2])
                indx += 1
    def _CalculateLength(self,event):

        DictDim ={}

        for item in activePartlist:
            curKey=item[1].ProfileShape+' '+item[1].Dimension
            if curKey in DictDim:
                DictDim[curKey]  +=item[1].Quantity * item[1].Length
                #DictDim[curKey]  += item[1].Length # custom requirement
            else:
                DictDim[curKey] = item[1].Quantity * item[1].Length
                #DictDim[curKey]  = item[1].Length #custom requirement
            curKey =None
        content =""
        for i in DictDim.keys():

            content += str(i) + "->\t" + str(DictDim[i]/1000) +'m\n'

        title = ''' \n\nTotal Running Length\n'''
        title += '''=================================\n'''
##        for item in activePartlist:
##            if 'AdditionalQuantity' in item[1].__dict__:
##                content+= "Pos %s : %i "%(item[0],item[1].AdditionalQuantity)
        self.Display.SetValue(unicode(title + content))
##        pass
class plChecker(wx.App):
    """
    The main wx App
    This is kept simple because i don't know how to do more here
    This will keep the GUI app alive
    """
    def __init__(self):
        wx.App.__init__(self,True)
    def OnInit(self):
        return True
def DB():
    global dbpath
    path =r'C:\PY\Excercises\Partlist_Checker'
##
##    patt = re.compile('^Plates[0-9]{4}\.db')
##    _fil = []
##    for f in curFiles:
##        #print patt.match(f)
##        if re.search(patt,f):
##            _fil.append(f)
##
##
##    dlg = wx.SingleChoiceDialog(None,
##    'UNIT',
##    'Unit Selection',
##    _fil)
##
##    if dlg.ShowModal() == wx.ID_OK:
##        _fname = dlg.GetStringSelection()
##    patt = re.compile('[0-9]{4}')
##    f = patt.search(_fname)
##    _Unit = f.group()
##    dbpath = path+'\\Plates'+_Unit+'.db'
##    print dbpath
    wildcard = "DB Files (*.db)|*.db|" \
    "Python sile (*.py)|*.py|" \
    "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a Db", path,
    "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        dbpath =dialog.GetPath()
    dialog.Destroy()
    _fdb = shelve.open(dbpath)
    _dbList = _fdb.keys()
    dlg = wx.SingleChoiceDialog(None,
    'DB',
    'DB Selection',
    _dbList)

    if dlg.ShowModal() == wx.ID_OK:
        _dbname = dlg.GetStringSelection()
    print _dbname
    _partlist = _fdb[str(_dbname)]
    _fdb.close()
    return _partlist
def dbUpdate(pl):
    print "inpa",dbpath
    try:
        db = shelve.open(dbpath)
        db['checking']=pl


        db.close()
    except:
        print Exception.message


if __name__ == '__main__':
    mytestApp = plChecker()     #test app used for development
    activePartlist = DB()
    testFr = mainWindow(activePartlist)
    testFr.Show()
    mytestApp.MainLoop()
