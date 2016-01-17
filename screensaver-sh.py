import launchpad
from pygame import time
from time import gmtime, strftime
from subprocess import call
import random

lp = launchpad.Launchpad()
lp.Open()

call(["clear"])
while 1:
 where_sccontrol = open("config/sccontrol.txt").read()
 where_sendstring = open("config/sendstring.txt").read()
 where_color = open("config/color.txt").read()
 where_sccontrol = where_sccontrol[:-1]
 where_sendstring = where_sendstring[:-1]
 where_color = where_color[:-1]
 call(["rm", "sccontrol.txt"])
 call(["wget", "-t", "0", where_sccontrol])
 sccontrol = open("sccontrol.txt").read()
 if "On" in sccontrol:
     print("SCCONTROL = ON")
     for i in range(3):
      for i in range(121):
          lp.LedCtrlRaw(i,3,0)
          time.wait(3)
      for i in range(121):
          lp.LedCtrlRaw(i,3,3)
          time.wait(3)
      for i in range(121):
          lp.LedCtrlRaw(i,0,3)
          time.wait(3)          
     lp.Reset()
     for i in range(3,5):
      for j in range(4,6):
         lp.LedCtrlXY(i, j, 3, 0)
         time.wait(5)
     time.wait(10)
     for i in range(3,5):
      for j in range(4,6):
         lp.LedCtrlXY(i, j, 3, 3)
         time.wait(5)
     time.wait(10)
     for i in range(3,5):
      for j in range(4,6):
         lp.LedCtrlXY(i, j, 0, 3)
         time.wait(5)
     time.wait(10)
     for i in range(2,6):
      for j in range(3,7):
         lp.LedCtrlXY(i, j, 3, 0)
         time.wait(5)
     time.wait(10)
     for i in range(2,6):
      for j in range(3,7):
         lp.LedCtrlXY(i, j, 3, 3)
         time.wait(5)
     time.wait(10)
     for i in range(2,6):
      for j in range(3,7):
         lp.LedCtrlXY(i, j, 0, 3)
         time.wait(5)
     for i in range(1,7):
      for j in range(2,8):
         lp.LedCtrlXY(i, j, 3, 0)
         time.wait(5)
     time.wait(10)
     for i in range(1,7):
      for j in range(2,8):
         lp.LedCtrlXY(i, j, 3, 3)
         time.wait(5)
     time.wait(10)
     for i in range(1,7):
      for j in range(2,8):
         lp.LedCtrlXY(i, j, 0, 3)
         time.wait(5)
     time.wait(10)
     for i in range(0,8):
      for j in range(1,9):
         lp.LedCtrlXY(i, j, 3, 0)
         time.wait(5)
     time.wait(10)
     for i in range(0,8):
      for j in range(1,9):
         lp.LedCtrlXY(i, j, 3, 3)
         time.wait(5)
     time.wait(10)
     for i in range(0,8):
      for j in range(1,9):
         lp.LedCtrlXY(i, j, 0, 3)
         time.wait(5)
# for i in range(11):
#     lp.LedAllOn(3,3)
#     for i in range(2500):
#      lp.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
#      time.wait(5)
     for i in range(121):
      lp.LedCtrlRaw(i,0,0)
      time.wait(5)
     lp.Reset()
     chour = int(strftime("%H", gmtime()))
     chour += 1
     lp.LedCtrlString(strftime(str(chour)+":%M", gmtime()),1,3,-1)
 elif "sendstring" in sccontrol:
   print("SCCONTROL = SENDSTRING")
   call(["rm", "sendstring.txt"])
   call(["wget", "-t", "0", where_sendstring])
   sendstring = open("sendstring.txt").read()
   if "Off" not in sendstring:
    print("SENDSTRING != OFF")
    call(["rm", "color.txt"])
    call(["wget", "-t", "0",where_color])
    color = open("color.txt").read()
    if "color=yellow" in color:
     print("COLOR = YELLOW")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,3,3,-1)
    elif "color=light_yellow" in color:
     print("COLOR = LIGHT_YELLOW")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,2,3,-1)
    elif "color=light_green" in color:
     print("COLOR = LIGHT_GREEN")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,1,3,-1)
    elif "color=green" in color:
     print("COLOR = GREEN")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,0,3,-1)
    elif "color=orange" in color:
     print("COLOR = ORANGE")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,3,1,-1)
    elif "color=light_orange" in color:
     print("COLOR = LIGHT_ORANGE")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,3,2,-1)
    elif "color=red" in color:
     print("COLOR = RED")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,3,0,-1)
    else:
     print("COLOR NOT RECOGNIZED, SO SET IT TO YELLOW")
     print("PLOTTING " + sendstring)
     lp.LedCtrlString(sendstring,3,3,-1)
   else:
    print("SENDSTRING = OFF")
    time.wait(5000)
 else:
     time.wait(5000)
