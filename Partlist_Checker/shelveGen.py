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
import csv,shelve,os
from Materials import Part,PartList,Plate
os.chdir(r'C:\PY\Excercises\Partlist_Checker')
def genPartlist(u):
    """
    Required by genDB

    """
    inpFile =  open('fs'+u+'plate.csv','r')
    reader = csv.reader(inpFile)

    ProfileList=PartList()
    for row in reader:
    ##        def __init__(self,pos,quat,thk,desc,wgt,nestname)
        quanTity = int(row[1])  #+int(row[2])
#Plate Part(Position Number, Quantity, Thickness, Description, Weight, ActcutName)
        curPos = Plate(str(row[0]),quanTity,row[3],row[2],float(row[5]),row[6])
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
    db = shelve.open('Plates'+u+'.db')
    PL = genPartlist(u)
    db['U'+u]=PL
    db.close()
    pass
if __name__ == '__main__':
    Unit ='5311'
    genDB(Unit)