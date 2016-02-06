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
 conn.send("Welcome to Sessho's Launchpad @ 33c3 | Admin Console. Type in password:\n")
 while 1:
    data = conn.recv(1024)
    if not data: break
    print "Empfangen: ", data
    if data[:-2] is "SumMerWars09":
     conn.send("Password accepted.")
     conn.send(">>>")  # echo
     while 1:
      data = conn.recv(1024)
      if not data: break
      if data[:-2] is "ledon":
       conn.send("\nLed Number: ")
       while 1:
        lednum = conn.recv(1024)
        if not lednum: break
        conn.send("\nColor code: ")
        while 1:
         colors = conn.recv(1024)
         if not colors: break
         red = colors[0]
         green = colors[1]
         try:
          lp.LedCtrlRaw(lednum,red,green)
         except:
          print("\nError.\n")
    else:
     conn.send("Password wrong. Kicking client.")
    conn.close()
    text = data
    text = data.replace(" ","")

while 1:
 conn, addr = s.accept()
 print('Mit ' + addr[0] + ' auf Port ' + str(addr[1]) + ' verbunden.')
 start_new_thread(clientthread,(conn,))
s.close()
