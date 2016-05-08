#!/usr/bin/python

import hashlib
import hmac
import sys
import random

host = sys.argv[1]
port = sys.argv[2]
public_key = sys.argv[3]
salt = ''.join([chr(int(random.uniform(0,255))) for i in range(0,20)])

print '|1|%s|%s %s'%(salt.encode('base64').strip(), hmac.new(salt, '[%s]:%s'%(host, port), hashlib.sha1).digest().encode('base64').strip(), public_key)
