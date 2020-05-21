
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Main():
    pass


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    
    
if __name__ == '__main__':
    main()
    
    