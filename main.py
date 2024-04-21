import random
# importing required librarie
import sys
import winsound
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QTimer, QTime, Qt
import functions
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second



class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.PasueFlag = False
    self.MAXTIME = 180000
    self.RESTTIME = 0
    self.STUDYTIME = 0
    self.total_time = 0
    self.learnig = 0
    self.all_time = 0

    self.setGeometry(100, 100, 800, 400)
    # creating a vertical layout
    layout = QVBoxLayout()
    self.labels = functions.Timelabel(80, 40)

    layout.addWidget(self.labels.label_time)
    layout.addWidget(self.labels.rest_time)
    layout.addWidget(self.labels.whole_time)
    layout.addWidget(self.labels.learning_time)
    self.setLayout(layout)

    self.realTimer = QTimer(self)
    self.realTimer.timeout.connect(self.showTime)
    self.realTimer.start(1000)
    self.restTimer = QTimer(self)
    self.restTimer.timeout.connect(self.restTime)
    self.restTimer.start(1000)

  # method called by timer
  def showTime(self):
    current_time = QTime.currentTime()
    realtime = current_time.toString('hh:mm')
    self.labels.label_time.setText(realtime)


  def restTime(self):
    if not self.PasueFlag:
      self.total_time += 1
      self.labels.whole_time.setText("总时间：" + str(int(self.total_time / 60)))
      if(self.RESTTIME == 0 and self.STUDYTIME == 0):
        study = random.randint(7, 10)
        self.STUDYTIME = study * 60

      if(self.STUDYTIME != 0): 
        self.STUDYTIME -= 1
        self.learnig += 1
        if(self.STUDYTIME == 0):
          rest = random.randint(1, 3)
          self.RESTTIME = rest * 60
          winsound.Beep(frequency, duration)
        self.labels.rest_time.setText("学习: " + str(self.STUDYTIME))
      elif(self.RESTTIME != 0):
        self.RESTTIME -= 1
        if(self.RESTTIME == 0):
          study = random.randint(7, 10)
          self.STUDYTIME = study * 60
          winsound.Beep(frequency, duration)
        self.labels.rest_time.setText("休息: " + str(self.RESTTIME))

      self.labels.learning_time.setText("学习时间： " + str(int(self.learnig / 60)))
      if(self.all_time >= 1800):
        self.RESTTIME = 600
        self.STUDYTIME = 0
        winsound.Beep(frequency, duration)

  def keyPressEvent(self, event):
    if event.key() == Qt.Key.Key_Space:
      self.PasueFlag = ~self.PasueFlag

App = QApplication(sys.argv)
window = Window()
winsound.Beep(frequency, duration)
window.show()
App.exit(App.exec())
