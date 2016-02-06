import socket
import sys
from thread import *
import launchpad
HOST = ''
PORT = 1337
BUFFER_SIZE = 10
lp = launchpad.Launchpad()
lp.Open()
text = ""
ledx = 1
ledy = 1

def ledch(x,y):
 lp.Reset()
 lp.LedCtrlXY(x,y,3,3)

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
 conn.send("Welcome to Sessho's Launchpad @ 33c3 >> Infinite. Type in text:\n")
 while 1:
    data = conn.recv(1024)
    if not data: break
    print "Empfangen: ", data
    #conn.send("KTHXBYE!\n")  # echo
    #conn.close()
    if data[:-2] is "w":
     if ledy >= 0:
      ledy -= 1
      ledch(ledx,ledy)
    elif data[:-2] is "a":
     if ledx >= 0:
      ledx -= 1
      ledch(ledx,ledy)
    elif data[:-2] is "s":
     if ledy <= 8:
      ledy += 1
      ledch(ledx,ledy)
    elif data[:-2] is "d":
     if ledx <= 7:
      ledx += 1
      ledch(ledx,ledy)
    elif data[:-2] is "c":
     conn.close()

ledch(ledx,ledy)
while 1:
 conn, addr = s.accept()
 print('Mit ' + addr[0] + ' auf Port ' + str(addr[1]) + ' verbunden.')
 start_new_thread(clientthread,(conn,))
s.close()
