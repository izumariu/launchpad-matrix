import launchpad
from pygame import time
lp = launchpad.Launchpad()
lp.Open()
color = "yellow"
BUFFER_TIME = 20
MOTTO = "Our Dreams"

def ledline(x,y):
 if color is "yellow":
  for i in range(x,(y+1)):
   lp.LedCtrlRaw(i,3,3)
 elif color is "green":
  for i in range(x,(y+1)):
   lp.LedCtrlRaw(i,0,3)
 elif color is "red":
  for i in range(x,(y+1)):
   lp.LedCtrlRaw(i,3,0)
 else:
  for i in range(x,(y+1)):
   lp.LedCtrlRaw(i,3,3)

def ledon(lednum):
 if color is "yellow":
  lp.LedCtrlRaw(lednum,3,3)
 elif color is "green":
  lp.LedCtrlRaw(lednum,0,3)
 elif color is "red":
  lp.LedCtrlRaw(lednum,3,0)
 else:
  lp.LedCtrlRaw(lednum,3,3)

def schar(char):
 lp.LedCtrlString(char,1,3,-1)
 time.wait(500)
 lp.Reset()
 time.wait(100)

while 1:
 lp.Reset()
 #FILL UP BACKGROUND VISIBLY
 for i in range(0,8):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(16,24):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(32,40):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(48,56):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(64,72):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(80,88):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(96,104):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 for i in range(112,120):
  lp.LedCtrlRaw(i,0,1)
  time.wait(BUFFER_TIME)
 time.wait(1000)
 #FIRST 3
 color = "yellow"
 ledline(0,3)
 ledon(18)
 ledon(19)
 ledon(35)
 ledline(48,51)
 time.wait(750)
 #SECOND 3
 color = "green"
 ledline(4,7)
 ledon(22)
 ledon(23)
 ledon(39)
 ledline(52,55)
 time.wait(750)
 #FIRST C
 color = "red"
 ledline(64,67)
 ledon(80)
 ledon(96)
 ledline(112,115)
 time.wait(750)
 #LAST 3
 color = "yellow"
 ledline(68,71)
 ledon(86)
 ledon(87)
 ledon(103)
 ledline(116,119)
 time.wait(3000)
 lp.Reset()
 #SHOW CHARS IN DETAIL
 schar("33C3")
 lp.LedCtrlString(MOTTO + " ",3,2,-1)
 time.wait(500)
