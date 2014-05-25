#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     25/11/2013
# Copyright:   (c) binoy.pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

_maintree = os.walk(r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D')
_L =[]

def isRecEmpty(path):

    _tree = os.walk(path)
    _f = next(_tree)
    print "f1:",_f[1]
    print "f2:",_f[2]
    if _f[2]:
        return False
    else:
        if not (_f[1] or _f[2]):
            print "entered empty dir:" + path
            return True
        elif _f[1]:
            print "entered Recursion"
            if len(_f[1])>1:
                print "more two dir"
                return False
            else:
                return True and isRecEmpty(_f[0]+"\\"+_f[1][0])




for i in _maintree:
    if isRecEmpty(i[0]):
        cmd ='rmdir /s "'+ i[0]+'"'
        os.system(cmd)



##for i in _maintree:
##    #print i[1]
##    for j in i[1]:
##        isEmpty(i[0]+'\\'+ j,_L)
##        break
##    break