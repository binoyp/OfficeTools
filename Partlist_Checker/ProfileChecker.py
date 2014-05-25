#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     23/09/2013
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
#os.chdir(r'C:\PY\Excercises\Partlist_Checker')
#print sys.path
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
    5.  Print all
    6. Exit


################################################################################
    '''

    print page
    ret = raw_input("Enter choice :")
    try :

        return int(ret)
    except:
        page1


def Common_Menu_1(db,activePartlist,resp):

    while resp != 6:

        resp = page1()
        if resp ==1:

            p=1
            while p:
                p = raw_input("Profile No. :")

                if "." in p:
                    [p,n] = p.split(".")
                    p = str(p)
                    n = int(n)
                    try:
                        activePartlist.members[p].Count(n)
                        activePartlist[p]
                        db['checking']= activePartlist
                    except:
                        print Exception.message
                elif "-" in p:
                    try:
                        [s1,s2] = p.split("-")
                        _cou = int(s2)-int(s1)
##                        print s1,s2,_cou
                        for _p in range(_cou):
                            s1 = int(s1)
                            print "%i Checked"%s1
                            activePartlist.members[str(s1)].Count()
                            s1 +=1
                    except:
                        print "Error in continuous counting",Exception.message

                elif p == "":
                    p = None
                else:
                    p = str(p)
                    try:
                        activePartlist.members[p].Count()
                        activePartlist[p]
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

            while 1:
                T1 = raw_input("Enter Position No. \t:")
                try:
                    if T1=="":
                        break
                    activePartlist[str(T1)]

                except:
                    print Exception.message
                    break
            os.system('pause')

        if resp == 5:
            DictDim ={}
            os.system('cls')
            for item in activePartlist:
                curKey=item[1].ProfileShape+' '+item[1].Dimension
                if curKey in DictDim:
                    DictDim[curKey]  +=item[1].Quantity * item[1].Length
                    #DictDim[curKey]  += item[1].Length # custom requirement
                else:
                    DictDim[curKey] = item[1].Quantity * item[1].Length
                    #DictDim[curKey]  = item[1].Length #custom requirement
                curKey =None
            for i in DictDim.keys():

                print str(i) + "->\t" + str(DictDim[i]/1000) +'m'

            print ''' \n\nParts With Additional Quantities'''
            print '''================================='''
            for item in activePartlist:
                if 'AdditionalQuantity' in item[1].__dict__:
                    print "Pos %s : %i "%(item[0],item[1].AdditionalQuantity)



            os.system('pause')


def checkpage(u):

    db = shelve.open('Profile'+u+'.db')

    Uname ='checking'
    if Uname in db.keys():
        activePartlist = db[Uname]
        resp = 0
        Common_Menu_1(db,activePartlist,resp)
    else:
        print "No current work"
        resp = 6


    db.close()


def NewCheck(u):
    db = shelve.open('Profile'+u+'.db')

    Uname ='U'+u
    if Uname in db.keys():
        activePartlist = db[Uname]
        resp = 0
        Common_Menu_1(db,activePartlist,resp)
    else:
        print "No Unit work"
        resp = 6
##        Common_Menu_1(db,activePartlist,resp)

##    activePartlist.showUnchecked()



    db.close()


def delProg(u):
    db = shelve.open('Profile'+u+'.db')

    Uname ='checking'
    if Uname in db.keys():
        del db[Uname]
        print "Deleted"
    else:
        print "No current work"


def mainpage(u):
    #os.system('cls')
    print """
    #---------------------------------------------------------------------------
    # Name:        PARTLIST CHECKER
    # Purpose:     Profile List Checking
    # Author:      BINOY PILAKKAT
    # Copyright:   (c) binoy.pilakkat 2013
    # Licence:     GNU PUBLIC LICENCE
    #---------------------------------------------------------------------------
    ****************************************************************************
    *                                                                          *
    *                            %s                                          *
    *                                                                          *
    ****************************************************************************
    1.  Open fresh Partlist
    2.  Open Working partlist
    3.  Delete Current work
    4.  Exit
    """ %u
    r = raw_input("     Enter Your choice:")
    try:
        return int(r)
    except:
        pass
if __name__ == '__main__':
    curFiles = os.listdir(os.getcwd())

    for f in curFiles:

        if f[-2:] == 'db':
            print f
    Unit =str(raw_input("Unit Number\t:"))

    if 'Profile'+Unit+'.db' in curFiles:
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
        print "No Database file found"
        os.system('pause')

