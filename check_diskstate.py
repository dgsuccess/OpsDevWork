import subprocess
import sys
from subprocess import PIPE

def diskState():
    cmd = 'c:\Windows\System32\MegaCli64.exe -LdInfo -LALL -aAll|findstr State'
    a = subprocess.Popen(cmd, shell=True, stdout=PIPE)
    stdout, stderr = a.communicate()
    return stdout

def praserState():
    data = diskState()
    s = (data.split('\r')[0]).split(' ')[16]
    return s

def diskAlarm():
    rlt = praserState()
    OK = 0
    WARNING = 1
    CRICTICAL = 2
    UNKNOWN = 3
    if rlt == "Optimal":
        print "OK - Disk Raid State is %s !!" % rlt
        sys.exit(OK)
    else:
        print "CRICTICAL, Disk Raid State is %s !!" % rlt
        sys.exit(CRICTICAL)
        
def main():
    diskAlarm()

if __name__ == '__main__':
    main()
