import subprocess
import re

def tokenizeOutput(text):
    rgxStr='[\d]*\:[\d]*\:[\d]*\.[\d]* IP ([\d]*\.[\d]*.[\d]*\.[\d]*)\.(\w*|\d*) \> ([\d]*\.[\d]*.[\d]*\.[\d]*\.)(\w*|\d*)'
    x = re.search(rgxStr,text)
    if x == None:
        return 1
    hostIP=x[0]
    hostService=x[1]
    targetIP=x[2]
    targetService=x[3]
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
        if output == 0:
            print outputDict


except KeyboardInterrupt:
    exit()
