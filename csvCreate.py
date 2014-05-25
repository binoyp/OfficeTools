#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Binoy.Pilakkat
#
# Created:     25/03/2014
# Copyright:   (c) Binoy.Pilakkat 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
f = open('C:\\pointsfromautocad.txt','r')
_lines = [ l.strip() for  l in f.readlines()]
f.close()
op =r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat' +'\\'+\
        _lines[0]+'.csv'
print op
f = open(op,'w')
for l in _lines[1:]:
    cl =  l[1:-1].split(' ')
    print cl
    f.write(",".join(cl)+'\n')

f.close()
k = raw_input("ok!")