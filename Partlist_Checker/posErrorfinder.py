#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     27/03/2014
# Copyright:   (c) binoy.pilakkat 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
d = []
for i in sys.path:
    if 'Tribon' in i:
        d.append(i)
for j in d:
    sys.path.remove(j)
import csv
from collections import namedtuple
f = open('pro.csv','r')
data = csv.reader(f)

header = data.next()
##print header
hd ={}
for (ind,val) in enumerate(header):
    v = str(val).capitalize()
##    print type(v),v
    hd.setdefault(v,ind)
_proDat = list(data)[1:]

print hd.keys()
def res(tol):
    _dictM={}
    _dictOut={}
    for r in _proDat:
        _cpr= _dictM.get(r[hd['Pos no']])
        if _cpr:
    ##        print abs(_cpr - float(r[hd['Length']]))
            if abs(_cpr - float(r[hd['Length']])) > float(tol) :
                dv = _dictOut.get(r[hd['Length']],0)+1
                _dictOut.setdefault(r[hd['Pos no']],dv)
        else:
             _dictM[r[hd['Pos no']]] = float(r[hd['Length']])
    return _dictOut

f.close()
_st=""

for i in range(11)[1:]:
    lt = res(float(i)).keys()
    if lt:
        _st += "\nFor Tolerance = "+str(i) +"\t Pos nos :" + str(lt)
    else:
        break
print _st
_q = raw_input('OutpUt to File? Y? Else press enter')
if _q:
    otfile = open('out.txt','w')
    otfile.write(_st)
    otfile.close()



