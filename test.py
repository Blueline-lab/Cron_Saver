import hashlib
import os
import config
import csv



        




a = os.popen("hostname").read()
b = str(a)[0:4]
if b == config.hostname:
    print("ok")


