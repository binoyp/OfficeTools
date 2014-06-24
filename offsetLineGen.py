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
import math,os,csv
csv.register_dialect('d1',lineterminator='\n')


def off(p,q,der,d =1):
    """
    Function to Calculate perpendicular point at d distance
    p,q -> x,y coordinate of the point of curve where derivative(slope) is der
    d -> offset distance [ d =0 gives ZeroDiv Error ]
    Return [x1,y1][x2,y2] -> [[Inside point][Outside point]]
    """
    m       =  - 1/der
##    p       =  820.5
##    q       =  2000


    C = d/(math.sqrt(m**2 + 1))

    x1 = p- C
    x2 = p + C

    y1 =q - (m*C)

    y2 = q + ( m*C)

    return [[x1,y1],[x2,y2]]


path =r"C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\OffsetLineConst"
outpath= r'C:\Documents and Settings\binoy.pilakkat\Desktop\D2D\SonarDomeDat\OffsetLineConst\out'

dlist = os.listdir(path)
for fil in dlist:

    inp = os.path.join(path,fil)
    if os.path.isfile(inp):

        f = open(inp,'r')
        of = open(os.path.join(outpath,fil),'w')
        oCsv=csv.writer(of,dialect='d1')
        rdr = csv.reader(f)
        dat = list(rdr)
        BWL = True
        for r in dat[1:]:
            ord = [ float(dec) for dec in r]
            print ord
            try:
                if ord [1]==0:

                    BWL =False
                if BWL:
                    ord[1] = -1*ord[1]
                [p1,p2]= off(ord[0],ord[1],ord[3],24)
                oCsv.writerow(ord+p1+p2)


            except ZeroDivisionError:
                oCsv.writerow(ord)
                print("Zero Error")
        of.close()



    f.close()
