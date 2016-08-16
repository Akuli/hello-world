#!/usr/bin/env python3

import os
import socket


a, b, c, d = os.pipe() + socket.socketpair()
if not os.fork():
    d.send(b'Hello World!\n')
elif os.fork():
    with open(a, 'r') as f:
        print(next(f))
else:
    with open(b, 'wb') as f:
        while not f.write(c.recv(1024)):
            pass
