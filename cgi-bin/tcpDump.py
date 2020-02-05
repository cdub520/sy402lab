import subprocess
import re

def tokenizeOutput(text):
    rgxStr='([\d]*\:[\d]*\:[\d]*\.[\d]*) IP ([\d]*\.[\d]*.[\d]*\.[\d]*)\.(\w*|\d*) \> ([\d]*\.[\d]*.[\d]*\.[\d]*\.)(\w*|\d*): Flags \[([SAFRPU.])*\],( seq \d*:\d*,)*( ack \d*,)*( win \d*,)*( options \[((\w*)|(\w*,))*.*])*, length \d*'
    x = re.search(rgxStr,text)
    print(x)
try:
    p = subprocess.Popen(('sudo', 'tcpdump', '-l'), stdout=subprocess.PIPE)
    for row in iter(p.stdout.readline, b''):
        tokenizeOutput(row)


except KeyboardInterrupt:
    exit()
