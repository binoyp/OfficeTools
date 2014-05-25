import os
ath = '\\\\amserver\\AMProjects\\FS4\\fsxmar\\SCH'
dirtree = os.walk(ath)
for i in dirtree:
    print len(i)