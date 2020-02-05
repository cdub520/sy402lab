#!/usr/bin/env python3
import glob
import os
import json
path='/home/tony/lab/*tcpDump.log'
filelist=glob.glob(path)
new=max(filelist,key=os.path.getctime)
fp=open(new,"r")
jsonObj=json.loads(fp.read())
print("Content-type: application/json\n\n{0}".format(json.dumps(jsonObj)))


