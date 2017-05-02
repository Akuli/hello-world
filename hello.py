#!/usr/bin/env python3
"""Print 'Hello World!' and exit."""

from posix import *
from io import *
from socket import *

globals().update(zip(map(chr, range(97,101)), pipe()+socketpair()))
if not (fork() and d.send(b'Hello World!\n') or fork() and print(next(open(++a,'r')))):
    while not open(--b,'wb').write(c.recv(1<<10)): { }
