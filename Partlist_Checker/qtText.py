#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Binoy.Pilakkat
#
# Created:     10/09/2013
# Copyright:   (c) Binoy.Pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import time
app = QApplication()
from PyQt4.QtCore import *
from PyQt4.QtGui import *
label = QLabel("<font color=red size=72><b>" + "message" + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000, app.quit) # 1 minute
app.exec_()