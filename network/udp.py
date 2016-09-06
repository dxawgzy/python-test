#! usr/bin/python
import socket, traceback, time, struct

port = 51423
host = ''

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while 1:
    try:
        message, address = s.recvfrom(8192)
        secs = int(time.time())
        secs = 60*60*24
        secs += 2208988800
        reply = struct.pack("!T". secs)
        s.sendto(reply, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()


