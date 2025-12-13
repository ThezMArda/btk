import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6 import QtGui
def Pencere():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Deneme Penceresi")
    etiket=QLabel(window)
    etiket.setText("sa")
    etiket.move(150,400)
    window.setGeometry(100,100,500,500)
    etiket2=QLabel(window)
    etiket2.setPixmap(QtGui.QPixmap("biz.png"))

    window.show()

    sys.exit(app.exec())
Pencere()
