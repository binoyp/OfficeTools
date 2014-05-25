
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
import sys,os,re
from scheme import SchemeFile,Panel,Bound,AttrDisplay
from Materials import Part,Plate
##d = []
##for i in sys.path:
##    if 'Tribon' in i:
##        d.append(i)
##for j in d:
##    sys.path.remove(j)
##os.chdir(r'C:\PY\Excercises\Partlist_Checker')
###print sys.path

import csv
import shelve,textwrap

def page1():
    os.system('cls')
    page ='''
##########################__Plate Check__#######################################
    1.  Start
    2.  Show Unchecked Data
    3.  Show Checked Data
    4.  Get a part detail
    5.  Plates with Excess
    6.  Add Excess
    7.  Add Comments
    8.  Thickness Sort
    9.  Nesting Information

################################################################################
    '''

    print page
    ret = raw_input("Enter choice :")
    try :

        return int(ret)
    except:
        page1
def Common_Menu_1(db,activePartlist,resp):
    while resp != 10:



        resp = page1()
        if resp ==1:

            p=1
            while p:
                p = raw_input("Position No. :")

                if "." in p:
                    [p,n] = p.split(".")
                    p = str(p)
                    n = int(n)
                    try:
                        activePartlist.members[p].Count(n)
                        activePartlist[p]

##                        Excs = raw_input("Add Excess Y/N")
##                        if Excs == "y":
##                            pe = raw_input("Add Exess ")
##                            activePartlist.members[p].AddExcess(pe)


##                        activePartlist[p]
                        db['checking']= activePartlist
                    except:
                        print Exception.message
                elif p == "":
                    p = None
                else:
                    p = p
                    try:
                        activePartlist.members[p].Count()
                        activePartlist[p]
##                        Excs = raw_input("Add Excess Y/N")
##                        if Excs == "y":
##                            pe = raw_input("Add Exess ")
##                            activePartlist.members[p].AddExcess(pe)


                        #activePartlist[p]
                        db['checking']= activePartlist
                    except:
                        print Exception.message



        if resp ==2:
            activePartlist.showUnchecked()
            os.system('pause')

        if resp ==3:
            activePartlist.showChecked()
            os.system('pause')
        if resp == 4:
            tr =1
            while tr:
                T1 = raw_input("Enter Position No. \t:")
                if T1 =="":
                    tr =0

                try:
                    activePartlist[str(T1)]
                    curItem =activePartlist.members[str(T1)]
                    _Lfl_ = curItem.Description.lower().split('-')
                    inpPan = '-'.join(_Lfl_[:-1])
                    print inpPan
                    try:


                        curSch_ = SchemeFile(inpPan)
                        curSch_.PanelDetails()
                        curSch_.BoundaryDetails()
                        try:
                            curSch_.ExcesDetails()
                        except:
                            print "No Excess Found in Scheme"
                    except:
                        print "Scheme Error"





                except:
                    print Exception.message





        if resp == 5:
            activePartlist.ShowGreenMaterial()
            W = raw_input("Press Enter to ContinuE..")

        if resp == 6:
            p=1
            while p:
                p = raw_input("Add Exess to Plate [pos.side]:")

                if "," in p:
                    [p,n] = p.split(",")
                    p = str(p)
                    n = str(n)
                    try:
                        activePartlist.members[p].AddExcess(n)
                        db['checking']= activePartlist
                        activePartlist[p]
                    except:
                        print Exception.message
                elif p == "":
                    p = None
                else:
                    print "Wrong Format"

            db['checking']= activePartlist
        if resp ==7:
                p = raw_input("Add Comments to Plate [pos,Comments]:")

                if "," in p:
                    [p,n] = p.split(",")
                    p = str(p)
                    n = str(n)
                    try:
                        activePartlist.members[p].AddComment(n)
                        db['checking']= activePartlist
                        activePartlist[p]
                    except:
                        print Exception.message
                elif p == "":
                    p = None
                else:
                    print "Wrong Format"

                db['checking']= activePartlist
        if resp == 8:
            DictThickness = {}
            os.system('cls')
            for item in activePartlist:
                curKey=item[1].Thickness
                if curKey in DictThickness:
                    DictThickness[curKey]  +=[item[1].Position+' -> '+\
                    item[1].ActCutName]
                else:
                    DictThickness[curKey] = [item[1].Position+' -> '+\
                    item[1].ActCutName]
                curKey =None
            print DictThickness.keys()
            thk = raw_input('Thickness:')
            if thk in sorted(DictThickness.keys()):
                outList =sorted(DictThickness[thk])

                print  'Thickness :',thk,'\n',\
                "\n".join(outList)
            os.system('pause')
        if resp ==9:
            DictPlate ={}
            os.system('cls')
            for item in activePartlist:
                curKey = item[1].ActCutName
                if not curKey in DictPlate:
                    DictPlate[curKey]=[]
            print "Plate List"
            #EnumPl = enumerate(sorted(DictPlate.keys()))
            for i in  enumerate(sorted(DictPlate.keys())):

                print str(i[0]),'-',i[1]
            print "\n Use ',1' to OutputTxtfile"
            inptP = raw_input('\nSelect Plate from the above List:')
            if ',' in inptP:
                Linp = str(inptP).split(',')
                bPrint=Linp[1]
                rP = Linp[0]
            else:
                rP = inptP
                bPrint =None


            try:
                print dict(enumerate(sorted(DictPlate.keys())))[int(rP)]
                for item in activePartlist:
                    curKey = dict(enumerate(sorted(DictPlate.keys())))[int(rP)]
                    if item[1].ActCutName == curKey:
                        if bPrint=='1':
                            fname='Plate'+str(curKey)+'.txt'
                            fOut = open(fname,'a')
                            wrStr = str(item[1].Position)+'\t'\
                            +item[1].Description+'\n'
                            fOut.write(wrStr)
                            fOut.close()
                        print item[1].Position+ '\t' + item[1].Description
            except:
                print Exception.message
            os.system('pause')


    bckdb = shelve.open('Backup.db')
    bckdb['checking']= activePartlist
    bckdb.close()

def checkpage(u):

    db = shelve.open('Plates'+u+'.db')

    os.system('pause')
    Uname ='checking'
    if Uname in db.keys():
        activePartlist = db[Uname]
        resp = 0
        Common_Menu_1(db,activePartlist,resp)
    else:
        os.system('cls')
        print "No current work"
        resp = 10

##    activePartlist.showUnchecked()

    db.close()


def NewCheck(u):
    db = shelve.open('Plates'+u+'.db')

    Uname ='U'+u
    if Uname in db.keys():
        activePartlist = db[Uname]
        resp = 0
        Common_Menu_1(db,activePartlist,resp)
    else:
        print "No Unit work"
        resp = 10

    db.close()





def delProg(u):
    db = shelve.open('Plates'+u+'.db')

    Uname ='checking'
    if Uname in db.keys():
        del db[Uname]
        os.system('cls')
        print "Current Work Deleted"
    else:
        os.system('cls')
        print "No Ongoing Checking"


def mainpage(rru):
    #os.system('cls')
    print """
    #---------------------------------------------------------------------------
    # Name:        PARTLIST CHECKER
    # Purpose:     Plate List Checking
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
    print str(rru) +'\n'
    r = raw_input("     Enter Your choice:")
    try:
        return int(r)
    except:
        pass
if __name__ == '__main__':
    curFiles = os.listdir(os.getcwd())
    patt = re.compile('^Plates[0-9]{4}\.db')
    for f in curFiles:
        #print patt.match(f)
        if re.search(patt,f):
            print f
    Unit =str(raw_input("Unit Number\t:"))

    if 'Plates'+Unit+'.db' in curFiles:

        resp = 5
        while resp != 4:
            resp = mainpage(Unit)
            if resp == 1:
                NewCheck(Unit)
            elif resp ==2:
                checkpage(Unit)
            elif resp ==3:
                delProg(Unit)
    else:
        print "No DB Found"
        os.system('pause')


