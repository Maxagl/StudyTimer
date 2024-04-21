from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtGui import QFont, QKeyEvent
from PySide6.QtCore import QTimer, QTime, Qt
class Timelabel():
  def __init__(self, fontsizeLarge, fontsizeSmall):
    self.label_time = QLabel()
    self.rest_time = QLabel()
    self.learning_time = QLabel()
    self.whole_time = QLabel()
    font = QFont('Arial', fontsizeLarge, QFont.Bold)
    font2 = QFont('Arial', fontsizeSmall, QFont.Bold)
    self.label_time.setAlignment(Qt.AlignCenter)
    self.label_time.setFont(font)

    self.rest_time.setAlignment(Qt.AlignCenter)
    self.rest_time.setFont(font)

    self.learning_time.setAlignment(Qt.AlignLeft)
    self.learning_time.setFont(font2)

    self.whole_time.setAlignment(Qt.AlignLeft)
    self.whole_time.setFont(font2)
