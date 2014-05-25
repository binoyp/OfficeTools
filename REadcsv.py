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

import csv
##outfile =open()
reader = csv.reader(open(r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\Tuesday- August 06- 2013\1401 Offsets\Book1.csv', "rb"))
writer = csv.writer(open(r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\Tuesday- August 06- 2013\1401 Offsets\out1.csv', "wb"))
p =[]
wl = [None]
i = True
for row in reader:
    if row[0]:
        print row
        writer.writerow(row)
    if row[1]:
        if row[1]!='Frame':

            ##print row[1:]
##            t = row[1:]
            t =[row[1]]+ [round(float(i)) for i in row[2:]]
            print t
            writer.writerow(t)
exit


##outfile.close()
##    print row#[0] != '' and row[1] !=''
##    print row[0] != '' and row[1] !=''
##    if row[0] != '' or row[1] !='':
##        print row


           ##print('true')
##    print row[0], row[-1]

##for row in someiterable:
##writer.writerow(row)