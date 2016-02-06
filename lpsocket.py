import socket
import sys
from thread import *
import launchpad
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
    #text = data.replace(" ","")
    lp.LedCtrlString(text[:-2] + "  ",1,3,-1)

while 1:
 conn, addr = s.accept()
 print('Mit ' + addr[0] + ' auf Port ' + str(addr[1]) + ' verbunden.')
 start_new_thread(clientthread,(conn,))
s.close()
