#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     08/02/2013
# Copyright:   (c) binoy.pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def factorial(n):
    r = 1
    while n > 0:
        r = r *n
        n = n -1
    return r
p =factorial(55)
print(p)
