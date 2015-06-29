#!/usr/bin/env python
# atoi

def atoi(s):
    if isinstance(s, basestring):
        return ord(s)
    else:
        return -1
