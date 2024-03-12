import random
# importing required librarie
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer, QTime, Qt


class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.MAXTIME = 180000
    self.RESTTIME = 0
    self.STUDYTIME = 0

    self.setGeometry(100, 100, 800, 400)
    # creating a vertical layout
    layout = QVBoxLayout()
    font = QFont('Arial', 120, QFont.Bold)
    self.label_time = QLabel()
    self.rest_time = QLabel()

    self.label_time.setAlignment(Qt.AlignCenter)
    self.label_time.setFont(font)

    self.rest_time.setAlignment(Qt.AlignCenter)
    self.rest_time.setFont(font)

    layout.addWidget(self.label_time)
    layout.addWidget(self.rest_time)
    self.setLayout(layout)

    self.realTimer = QTimer(self)
    self.realTimer.timeout.connect(self.showTime)
    self.realTimer.start(1000)

    self.restTimer = QTimer(self)
    self.restTimer.timeout.connect(self.restTime)
    self.restTimer.start(1000)


    self.current_time = 0
    self.last_time = 0
    self.all_time = 0

  # method called by timer
  def showTime(self):
    current_time = QTime.currentTime()
    realtime = current_time.toString('hh:mm')
    self.label_time.setText(realtime)

  def restTime(self):
    if(self.RESTTIME == 0 and self.STUDYTIME == 0):
      study = random.randint(7, 10)
      self.STUDYTIME = study * 6
    self.last_time = self.current_time
    rawtime = QTime.currentTime()
    self.current_time = rawtime.hour() * 60 * 60 + rawtime.minute() * 60 + rawtime.second()

    if(self.STUDYTIME != 0): 
      self.STUDYTIME -= 1
      self.all_time += 1
      if(self.STUDYTIME == 0):
        rest = random.randint(1, 3)
        self.RESTTIME = rest * 6
      self.rest_time.setText("学习: " + str(self.STUDYTIME))
    elif(self.RESTTIME != 0):
      self.RESTTIME -= 1
      if(self.RESTTIME == 0):
        study = random.randint(7, 10)
        self.STUDYTIME = study * 6
      self.rest_time.setText("休息: " + str(self.RESTTIME))

    if(self.all_time >= 180):
      self.all_time = 0
      self.RESTTIME = 60
      self.STUDYTIME = 0


App = QApplication(sys.argv)
window = Window()
window.show()
App.exit(App.exec())
