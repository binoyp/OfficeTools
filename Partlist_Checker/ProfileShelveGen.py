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
import csv,shelve,os

os.chdir(r'C:\PY\Excercises\Partlist_Checker')
from Materials import Part,PartList,Profile
def genPartlist(u):
    inpFile =  open('fs'+u+'pro.csv','r')
    reader = csv.reader(inpFile)

    ProfileList=PartList()
    for row in reader:
    ##        print row[:4]
        quanTity = int(row[1])+int(row[2])
    ##        print quanTity
        curPos = Profile(str(row[0]),quanTity,str(row[3]),row[4],float(row[6]),float(row[7]))

    ##        print curPos
        ProfileList.addMember(curPos)
    return ProfileList
def genDB(u):
    """

    Run this Only when starting a new partlist check
    to create a partlist db file
    I know this stuff ;-)
    ^-^ ^-^ ^-^

    """
    db = shelve.open('Profile'+u+'.db')
    PR = genPartlist(u)
    db['U'+u]=PR
    db.close()
    pass
if __name__ == '__main__':
    #Change the following line
    Unit ="0621"
    genDB(Unit)
