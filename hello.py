#!/usr/bin/env python3
"""Print 'Hello World!' and exit."""

from posix import *
from io import *
from socket import *

globals().update(zip(map(chr, range(97,101)), pipe()+socketpair()))
if not fork(): d.send(b'Hello World!\n')
elif fork(): print(next(open(++a,'r')))
else:
    # the pass keyword is useless
    while not open(--b,'wb').write(c.recv(1<<10)): { }
