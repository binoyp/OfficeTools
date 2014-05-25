#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Binoy.Pilakkat
#
# Created:     27/09/2013
# Copyright:   (c) Binoy.Pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import os,re
class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return '\n '.join(attrs)
    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.gatherAttrs())


class Panel(AttrDisplay):
    def __init__(self,pnl):

        _lPnst_ = pnl.split(', ')
        self.SIDE = _lPnst_[2]
        self.BLO = _lPnst_[3][4:]
        self.LOC = _lPnst_[5][4:]
class Bound:
    def __init__(self,_bouStmnt_):
        self._Limits_ = _bouStmnt_[4:].split('/')
        self._nBou_ = len(self._Limits_)+1
    def __str__(self):
        _outStr_ =''
        for i in range(self._nBou_-1):
            self._Limits_[i]=self._Limits_[i].strip()
            _outStr_ += ("Limit %i -->\t "%(i+1)+str(self._Limits_[i]))+'\n'
        return _outStr_
    def __getitem__(self,i):
        if i < len(self._Limits_):
            return self._Limits_[i]
        else:
            return "Out of Range"

class SchemeFile:


    def __init__(self,_part_name_,_search = False):
        _SchemePath ='\\\\amserver\\AMProjects\\FS4\\fsxmar\\SCH'

        _SchemeFile_ = _SchemePath + '\\'+_part_name_+".sch"
        if  not os.path.exists(_SchemeFile_):
            _SchemeFile_ = _SchemePath + '\\'+_part_name_


        #print _SchemeFile_
        try:

           _Sch_ = open(_SchemeFile_,'r')
        except:
            print "File not found"
            _Sch_= None
            assert False,'F'
        if _Sch_:

            _content_= _Sch_.read()
            #print _content_



            self._statments_= _content_.split(';')
            _bouStmnt_ =[_st_.strip() for _st_ in self._statments_ if _st_.strip()\
            [:3]=='BOU'][0]
            self.Boundary = Bound(_bouStmnt_)
        if _search:
            dirtree = os.walk(_SchemePath)

##
##
##            _Pan_=_stmnts_[0].split(', ')
##            print(_Pan_[5][4:])
        #else:
##            print "Am sorry"
##            self = None

    def PanelDetails(self):

        _pan_ = ""
        for i in self._statments_:
            _pan_ +=unicode(i)
        return _pan_

    def BoundaryDetails(self):
        return self.Boundary

    def ExcesDetails(self):
        _Exc_ = [_st_.strip() for _st_ in self._statments_ if _st_.strip()[:3]\
        =='EXC']
        #print _Exc_
        out =""
        for _E in _Exc_:
            _lExc_ = _E.split(', ')

            out +=  "Excess Type is applied on "+\
                str(_lExc_[1].strip()[4:])+"boundary"

            out += str(_lExc_[3])+"@"+\
                str(self.Boundary[int(_lExc_[2].strip()[4])-1])

        return out

if __name__ =='__main__':

    _part_name_ = 'fs0201-dkgr1500'.lower()
    curScheme =SchemeFile(_part_name_)
    print type(curScheme)
    if curScheme:
        curScheme.BoundaryDetails()
        curScheme.PanelDetails()
        curScheme.ExcesDetails()


##_Pan_ = [_st_.strip() for _st_ in _stmnts_[1:] if _st_.strip()[:3]=='PAN'][0]
##print _Pan_