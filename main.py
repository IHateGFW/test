import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
qgc = ('127.0.0.1', 14550)
msg = open("msg.log")
msglists = msg.readlines()
msgbuf = []
i = 0
while i < len(msglists)-2:
    for ch in msglists[i].replace("head:", "").rstrip('\n').split():
        msgbuf.append(int(ch,16))
    for ch in msglists[i + 1].replace("payload:", "").rstrip('\n').split():
        msgbuf.append(int(ch,16))
    for ch in msglists[i + 2].replace("ck:", "").rstrip('\n').split():
        msgbuf.append(int(ch,16))

    s.sendto(bytes(msgbuf),qgc)
    i = i + 3

