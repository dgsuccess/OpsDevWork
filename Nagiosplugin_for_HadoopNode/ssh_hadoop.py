#!/usr/bin/env python

import paramiko
import time

"""
Connect to a host and exec comm

"""



def ssh(comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.0.13',22)
    stdin,stdout,stderr = ssh.exec_command(comm)
#    for i in stdout.readlines():
#        print i,
    ssh.close()

def main():
    startcomm = "cd /usr/hadoop-1.0.2/bin/;sh start-all.sh"
    stopcomm = "cd /usr/hadoop-1.0.2/bin;sh stop-all.sh"
    ssh(stopcomm)
    time.sleep(10)
    ssh(startcomm)
    

if __name__ == "__main__":
    main()
