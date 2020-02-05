import subprocess
import re
from datetime import datetime
import json
def tokenizeOutput(text):
    rgxStr='([\d]+\.[\d]+.[\d]+\.[\d]+)\.(\w*|\d*) \> ([\d]+\.[\d]+.[\d]+\.[\d]+)\.(\w*|\d*)'
    x = re.search(rgxStr,text)
    print(x.group())
    input()
    if x == None:
        return 1
    hostIP=x.group(1)
    hostService=x.group(2)
    targetIP=x.group(3)
    targetService=x.group(4)
    if hostIP in outputDict:
        if hostService in outputDict[hostIP]:
            outputDict[hostIP][hostService] += 1
        else:
            outputDict[hostIP][hostService] = 1
    else:
        outputDict[hostIP]={hostService:1}
    return 0

try:
    outputDict={}
    p = subprocess.Popen(('sudo', 'tcpdump', '-l'), stdout=subprocess.PIPE)
    for row in iter(p.stdout.readline, b''):
        output = tokenizeOutput(str(row))


except KeyboardInterrupt:
    fp=open('/home/tony/lab/'+datetime.now().strftime("%H:%M:%S")+"tcpDump.log","w")
    fp.write(json.dumps(outputDict))
    exit()
