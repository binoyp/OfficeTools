#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     23/06/2014
# Copyright:   (c) binoy.pilakkat 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
import os,csv
csv.register_dialect('d1',lineterminator='\n')

def parser(inpt,outp):
    f = open(inp,'r')
    o = open(outp,'w')
    wrtr = csv.writer(o,dialect = "d1")

    h =['Y', 'Z', 'Angle', 'Derivative']
    wrtr.writerow(h)
    for row in f:

       s = row.strip()
       p = re.compile("[^\w.]*")
       rlist =  p.split(s)
       if len(rlist)>3:

        if rlist[0]<>'X':
            print rlist
            wrtr.writerow(rlist[1:])

    f.close()
path = r"C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\FrameDat"
opath =r"C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\OffsetLineConst"
dlist = os.listdir(path)
for fil in dlist:
    inp = os.path.join(path,fil)
    out = os.path.join(opath,fil)
    parser(inp,out)