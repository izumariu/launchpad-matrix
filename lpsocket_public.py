import socket
import sys
from thread import *
import launchpad
from pygame import time
HOST = ''
PORT = 8888
BUFFER_SIZE = 10
lp = launchpad.Launchpad()
lp.Open()
text = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket erstellt.'

try:
 s.bind((HOST, PORT))
except socket.error as msg:
 print 'Binden fehlgeschlagen. Errorcode : ' + str(msg[0]) + ' Message ' + msg[1]
 sys.exit()

print 'Binden des Sockets abgeschlossen.'
s.listen(10)
print 'Socket hoert jetzt die Nachrichten ab.'

def clientthread(conn):
 conn.send("Welcome to Sessho's Launchpad @ 33c3. Type text:\n")
 while 1:
    data = conn.recv(1024)
    if not data: break
    print "Empfangen: ", data
    conn.send("KTHXBYE!\n")  # echo
    conn.close()
    text = data
    text = data.replace(" ","")
    lp.Reset()
    lp.LedCtrlString(text[:-2] + "  ",1,3,-1)

while 1:
 for j in range(4):
  for i in range(121):
   lp.LedCtrlRaw(i,3,0)
  lp.LedCtrlString("3",3,0,0)
  time.wait(500)
  for i in range(121):
   lp.LedCtrlRaw(i,3,1)
  lp.LedCtrlString("3",3,1,0)
  time.wait(500)
  for i in range(121):
   lp.LedCtrlRaw(i,0,3)
  lp.LedCtrlString("C",0,3,0)
  time.wait(500)
  for i in range(121):
   lp.LedCtrlRaw(i,3,3)
  lp.LedCtrlString("3",3,3,0)
  time.wait(500)
 for i in range(121):
  lp.LedCtrlRaw(i,0,1)
 for i in range(3):
  conn, addr = s.accept()
  print('Mit ' + addr[0] + ' auf Port ' + str(addr[1]) + ' verbunden.')
  start_new_thread(clientthread,(conn,))
s.close()
