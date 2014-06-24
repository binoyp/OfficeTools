#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:
# Copyright:   (c) binoy.pilakkat
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import difflib,csv
def OffsetComp(f1,f2):
    f1 = open(r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\OffsetGreenLines\FR8-1125GREEN.csv','r')
    f2 = open(r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\BlueLines\FR8-1125BLUE.csv','r')

    rd1 = csv.reader(f1)
    rd2 = csv.reader(f2)

    cf1 = list(rd1)
    cf2 = list(rd2)
    dict1 ={}
    dict2={}
    for row in cf1:
        dict1[float(row[2])] =[float(val) for val in row[:2]]
    for row in cf2:
        dict2[float(row[2])] =[float(val) for val in row[:2]]


##    print dict1
##    print dict2
    f1.close()
    f2.close()

    fl = [cf1,cf2]
    common = set(dict1.keys()).intersection(set(dict2.keys()))
    of = open(r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\BG Comparison\fr8-1125.txt','w')
    of.write('FR8-1125\n')
    for z in sorted(common):
        #print dict1[z][1],dict2[z][1]
        diffX = abs(dict1[z][0])-abs(dict2[z][0])
        diffY = abs(dict1[z][1])-abs(dict2[z][1])
        text = "For Z=%(z)s, dX = %(x)s, dy = %(y)s\n"%{'z':z,"x":diffX,"y":diffY}
        of.write(text)
        print text

    of.close()
OffsetComp(0,0)