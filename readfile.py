#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      binoy.pilakkat
#
# Created:     15/02/2013
# Copyright:   (c) binoy.pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def fread(fname):
    file_object = open(fname)
    try:
        all_the_text = file_object.read( )
    finally:
        file_object.close( )
        print(all_the_text)
def main():
    fread('t.txt')
    pass

if __name__ == '__main__':
    main()
