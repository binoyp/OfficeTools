#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Binoy.Pilakkat
#
# Created:     10/09/2013
# Copyright:   (c) Binoy.Pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys,os
d = []
for i in sys.path:
    if 'Tribon' in i:
        d.append(i)
for j in d:
    sys.path.remove(j)
#os.chdir(r'C:\PY\Excercises\Partlist_Checker')
#print sys.path


import textwrap
class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return '\n '.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


class Part(AttrDisplay):
    def __init__(self,quan,quality,Pos,chk =False):
        self.Quality = quality
        self.Quantity = quan
        self.Position = Pos
        self.CHECKED = chk
        self.QuantityCount = 0


    def Check(self):
        self.CHECKED = True

    def Count(self,n=1):
        out =""
        if self.QuantityCount >= self.Quantity:
            self.QuantityCount += n
            out += "Quandity already reached"
            out += "Excess Quandity is :"+str(self.QuantityCount-self.Quantity)
            self.Check()
            self.AdditionalQuantity = self.QuantityCount-self.Quantity
        elif self.QuantityCount + n > self.Quantity:
            #print map(type,[self.QuantityCount,n])
            self.AdditionalQuantity = self.QuantityCount + n - self.Quantity
            out += "More Number"
        else:
            self.QuantityCount += n
            if self.QuantityCount==self.Quantity:
                self.Check()
            out += str(self.Position) +" Checked"
        return out

class Plate(Part):
    """
    Plate Part(Position Number, Quantity, Thickness, Description, Weight, ActcutName)
    """
    def __init__(self,pos,quat,thk,desc,wgt,nestname):
        Part.__init__(self, quan = quat,Pos =pos,quality = 'DMR249A')
        self.Thickness = thk
        self.Description = desc
        self.Weight = wgt
        self.ActCutName = nestname

        self.Excess = ""
        self.Comments=""
    def AddExcess(self,side):
        #S,P,T,B,Out,In,Aft,Fore
        if  side:
            self.Excess = side
        else:
            self.Excess = ""
    def AddComment(self,comm):
        self.Comments = comm
class Profile(Part):
    """
    Position , Quantity, Type , Dimension, Weight,Length
    """
    def __init__(self,pos,quat,typ,dim,wgt,len):
        Part.__init__(self,quan = quat,Pos =pos,quality = 'D40S',\
        chk =False)
        self.Dimension = dim
        self.Length = len
        self.ProfileShape = typ
        self.Weight = wgt


class PartList(AttrDisplay):
    """
    This part is not used for this file
    Used when generating db files
    """
    itKey =None

    def __init__(self):
        self.members = {}
    def addMember(self,part):

        if part.__class__.__name__ =='Profile':

            if part.Position in self.members:
                print "Repeating pos number"
                print (part.Position)
                #self.members[part.Position+'-i']=part
                print "DD" + str(self.members[part.Position].Quantity)
                self.members[part.Position].Quantity += part.Quantity
                self.members[part.Position].Weight += part.Weight
                self.members[part.Position].Length += part.Length

            else:
                self.members[part.Position]=part
        else:
            if part.Position in self.members:
                print "Nested in different Plates: %s \n"%part.ActCutName
                print (part.Position)
                #self.members[part.Position+'-i']=part
                print "DD" + str(self.members[part.Position].Quantity)
                self.members[part.Position].Quantity += part.Quantity
                self.members[part.Position].Weight += part.Weight
                if 'ActCutName2' in self.members[part.Position].__dict__.keys():
                    self.members[part.Position].ActCutName2 += '\n'+part.ActCutName
                else:
                    self.members[part.Position].ActCutName2 = part.ActCutName

            else:
                self.members[part.Position]=part

        #print self.members[part.Position]

    def showChecked(self):
        out= []

        for mem in self.members:
            if self.members[mem].CHECKED:
                out.append([mem,self.members[mem].QuantityCount,self.members[mem].Quantity])
                #print str(mem) +'\n'
##        outString += "Checked\n"
##        outString = textwrap.fill(outString,60)
##        outString = "Checked\n"+outString
        print out
        return out

    def showUnchecked(self):
        """
        [mem,self.members[mem].QuantityCount,self.members[mem].Quantity]
        """

        outString=""
        _filestr =[]
        #print self.members.keys()
        for mem in self.members.keys():
            ##print mem.__class__.__name__
            ##try:
            if not self.members[mem].CHECKED:
                outString += str(mem) +'\t'
                _filestr.append([mem,self.members[mem].QuantityCount,self.members[mem].Quantity])
##                _filestr += str(mem) +'\t'+str(self.members[mem].QuantityCount)+\

                    #print str(mem) +'\n'
        return _filestr
##        _q = raw_input("File ?")
##        if _q=='y':
##
##            f= open('C:\\UncheckedPartslist.txt','w')
##            try:
##                f.write(_filestr)
##                print "'C:\\UncheckedPartslist.txt' Successfully written"
##            except:
##                print "File ERror"
##            finally:
##                f.close()

    def __getitem__(self,pos):
        if pos in self.members:
##            _s = self.members[pos].__class__.__name__
            outString ="Position Number:"+str(pos)+'\n'
            if self.members[pos].__class__.__name__=='Plate':
                if self.members[pos].Thickness < 8.0:
                    outString += '''
                    No Bevel Info required
                    ----------------------
                        '''
                elif float(self.members[pos].Thickness) >= 8.0:
                    if float(self.members[pos].Weight) > 10.0:
                        outString += "\nBevel Required\n"
                if 'ActCutName2' in self.members[pos].__dict__.keys():
                    outString += "Part is nested in different Sheets\n"
                    outString += "----------------------------------\n"
                    outString += str(self.members[pos].ActCutName2)

                _s ='Actcutname:'+self.members[pos].ActCutName+'\n\t\tThickness:'+\
                str(self.members[pos].Thickness)+'\n\t\tWeight:'+str(self.members[pos].Weight)
            else:
                _s ='Dimension:%s\n\t\tLength:%f'%(self.members[pos].Dimension,\
                self.members[pos].Length)
            outString += "\t\tQuantity : "+str(self.members[pos].Quantity)\
            +"\n\t\tQuality  :"+self.members[pos].Quality+\
            "\n\t\t"+_s+\
            " \n\t\tChecked:"+str(self.members[pos].CHECKED)+\
            "\n\t\tQuantityChecked:"+ str(self.members[pos].QuantityCount)

            return unicode(outString)
    def TotalWeight(self):
        Wgt = 0
        for mem in self.members.keys():
            Wgt += float(self.members[mem].Weight)

        return Wgt
    def ShowGreenMaterial(self):
        OutStrin = ""
        print \
        """
        Plates with Excess

        """
        for mem in self.members.keys():
            if self.members[mem].Excess:
                #print type(self.members[mem].Excess),mem
                OutStrin += str(mem) + '\t'
        print textwrap.fill(OutStrin,80)
    def __iter__(self):
        return iter(self.members.items())



