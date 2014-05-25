#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     06/09/2013
# Copyright:   (c) binoy.pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys,os
d = []
for i in sys.path:
    if 'Tribon' in i:
        d.append(i)
for j in d:
    sys.path.remove(j)
os.chdir(r'C:\PY\Excercises\Partlist_Checker')
#print sys.path


##import textwrap
##class AttrDisplay:
##    """
##    Provides an inheritable print overload method that displays
##    instances with their class names and a name=value pair for
##    each attribute stored on the instance itself (but not attrs
##    inherited from its classes). Can be mixed into any class,
##    and will work on any instance.
##    """
##    def gatherAttrs(self):
##        attrs = []
##        for key in sorted(self.__dict__):
##            attrs.append('%s=%s' % (key, getattr(self, key)))
##        return ', '.join(attrs)
##    def __str__(self):
##        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
##
##
##class Part(AttrDisplay):
##    def __init__(self,quan,quality,Pos,chk =False):
##        self.Quality = quality
##        self.Quandity = quan
##        self.Position = Pos
##        self.CHECKED = chk
##        self.QuantityCount = 0
##
##
##    def Check(self):
##        self.CHECKED = True
##
##    def Count(self,n=1):
##        for num in range(1,n+1):
##            if self.QuantityCount == self.Quandity:
##                print "Quandity already reached"
##                self.Check()
##            else:
##                self.QuantityCount += 1
##                if self.QuantityCount == self.Quandity:self.Check()
##
##
##class Profile(Part):
##    def __init__(self,pos,quat,typ,dim,len):
##        Part.__init__(self,quan = quat,Pos =pos,quality = 'D40S',\
##        chk =False)
##        self.Dimension = dim
##        self.Length = len
##        self.ProfileShape = typ
##class Plate(Part):
##    def __init__(self,pos,quat,typ):
##        Part.__init__(quan = quat,Pos =pos,quality = 'DMR249A',Typ =typ)
##class PartList:
##
##    def __init__(self):
##        self.members = {}
##    def addMember(self,part):
##        if part.Position in self.members:
##            print "Already exists"
##        #print part.Position
##        self.members[part.Position]=part
##        #print self.members[part.Position]
##
##    def showChecked(self):
##        outString =""
##        for mem in self.members:
##            if self.members[mem].CHECKED:
##                outString += str(mem) + '\t'
##                #print str(mem) +'\n'
##        print textwrap.fill(outString,80)
##    def showUnchecked(self):
##
##        outString=""
##        #print self.members.keys()
##        for mem in self.members.keys():
##            ##print mem.__class__.__name__
##            ##try:
##            if not self.members[mem].CHECKED:
##                outString += str(mem) +'\t'
##                    #print str(mem) +'\n'
##        print textwrap.fill(outString, 80)
##    def getItem(self,pos):
##        if pos in self.members:
##            print self.members[pos]



import csv
import shelve
from Materials import Part,PartList,Profile



def page1():
    os.system('cls')
    page ='''
################################################################################
    1.  Start
    2.  Show Unchecked Data
    3.  Show Checked Data
    4.  Get a part detail
    5.  Exit


################################################################################
    '''

    print page
    ret = raw_input("Enter choice :")
    try :

        return int(ret)
    except:
        page1

def checkpage():

    db = shelve.open('Profile1424')

    Uname ='checking'
    if Uname in db.keys():
        activePartlist = db[Uname]
        resp = 0
    else:
        print "No current work"
        resp = 5

##    activePartlist.showUnchecked()

    while resp != 5:



        resp = page1()
        if resp ==1:

            p=1
            while p:
                p = raw_input("Profile No. :")

                if "," in p:
                    [p,n] = p.split(",")
                    p = str(p)
                    n = int(n)
                    try:
                        activePartlist.members[p].Count(n)
                        activePartlist.getItem(p)
                        db['checking']= activePartlist
                    except:
                        print Exception.message
                elif p == "":
                    p = None
                else:
                    p = str(p)
                    try:
                        activePartlist.members[p].Count()
                        activePartlist.getItem(p)
                        db['checking']= activePartlist
                    except:
                        print Exception.message



        if resp ==2:
            activePartlist.showUnchecked()
            t= raw_input("Press Enter")

        if resp ==3:
            activePartlist.showChecked()
            t= raw_input("Press Enter")
        if resp == 4:
            T1 = raw_input("Enter Position No. \t:")
            try:
                activePartlist.getItem(int(T1))

            except:
                print Exception.message
            T1 = raw_input("Press Enter")


    db.close()


def NewCheck():
    db = shelve.open('Profile1424')

    Uname ='U1424'
    if Uname in db.keys():
        activePartlist = db[Uname]
        resp = 0
    else:
        print "No Unit work"
        resp = 5

##    activePartlist.showUnchecked()

    while resp != 5:

        resp = page1()
        if resp ==1:

            p=1
            while p:
                p = raw_input("Profile No. :")

                if "," in p:
                    [p,n] = p.split(",")
                    p = str(p)
                    n = int(n)
                    try:
                        activePartlist.members[p].Count(n)
                        db['checking']= activePartlist
                        activePartlist.getItem(p)
                    except:
                        print Exception.message
                elif p == "":
                    p = None
                else:
                    p = str(p)
                    try:
                        activePartlist.members[p].Count()
                        activePartlist.getItem(p)
                        db['checking']= activePartlist
                    except:
                        print Exception.message

            db['checking']= activePartlist



        if resp ==2:
            activePartlist.showUnchecked()
            t= raw_input("Press Enter")

        if resp ==3:
            activePartlist.showChecked()
            t= raw_input("Press Enter")
        if resp == 4:

            T1 = raw_input("Enter Position No. \t:")
            try:
                activePartlist.getItem(str(T1))

            except:
                print Exception.message
            T1 = raw_input("Press Enter")

    db.close()





def delProg():
    db = shelve.open('Profile1424')

    Uname ='checking'
    if Uname in db.keys():
        del db[Uname]
        print "Deleted"
    else:
        print "NO current work"


def mainpage():
    #os.system('cls')
    print """
    #---------------------------------------------------------------------------
    # Name:        PARTLIST CHECKER
    # Purpose:      Assists in checking partlist
    #
    # Author:      BINOY PILAKKAT
    #
    # Created:     23/08/2013
    # Copyright:   (c) binoy.pilakkat 2013
    # Licence:     GNU PUBLIC LICENCE
    #---------------------------------------------------------------------------
    1.  Open fresh Partlist
    2.  Open Working partlist
    3.  Delete Current work
    4.  Exit
    """
    r = raw_input("     Enter Your choice:")
    try:
        return int(r)
    except:
        pass
if __name__ == '__main__':
    resp = 5
    while resp != 4:
        resp = mainpage()
        if resp == 1:
            NewCheck()
        elif resp ==2:
            checkpage()
        elif resp ==3:
            delProg()







##    PL = genPartlist()
##    db=shelve.open('Partlist')
##    db['U1414pro']= PL
##    db.close()    ##    page1='''

##
##    '''
##    print page1
##
##    PL.getItem(1)

##    ProfileList.showUnchecked()


