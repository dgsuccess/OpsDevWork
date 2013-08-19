#!/usr/bin/env python

###### Create by Victor 12/08/2013 #####

#coding:utf-8

import subprocess
import os
import time
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#Define variables

mail_to_list = ['guomin@gemside.com','25787003@qq.com']
websource_dir = '/var/www/html/'
backup_dir = '/var/www/backup/'
today = time.strftime("%Y%m%d", time.localtime())


#Define mysql database backup function

def mysqlBackup(user, password, dbname, backup_dir, today):
    cmd = "mysqldump -u%s -p%s --databases %s |gzip > %sjsdb_%s.sql.gz" % (user, password, dbname, backup_dir, today)
    rlt = subprocess.call(cmd,shell = True)
    if rlt == 0:
        status = "yes"
        download_addr = "www.gemside.net:8080/jsdb_%s.sql.gz" % today
        return status, download_addr
    else:
        status = "no"
        download_addr = "NULL,Please Contact Administrator"
        return status, download_addr

#Define website database backup function

def webpageBackup(websource_dir, backup_dir, today):
    cmd = "tar cvfz %sjsweb_%s.tar.gz %s" % (backup_dir, today, websource_dir)
    rlt = subprocess.call(cmd,shell = True)
    if rlt == 0:
        status = "yes"
        download_addr = "www.gemside.net:8080/jsweb_%s.tar.gz" % today
        return status, download_addr
    else:
        status = "no"
        download_addr = "NULL,Please Contact Administrator"
        return status,download_addr

#Define send backup resoult mail function

def sendMail(mail_to_list, dbstatus, db_dladdr, webstatus, web_dladdr):
    sender = 'gemsidewebsite@163.com'
    receiver = mail_to_list
    if dbstatus == 'yes' and webstatus == 'yes':
        backupinfo = "MySQL DB Backup is OK, WebPage Backup is OK!"
    elif dbstatus == 'yes' and webstatus == 'no':
        backupinfo = "MySQL DB Backup is OK, WebPage Backup is Failed!"
    elif dbstatus == 'no' and webstatus == 'yes':
        backupinfo = "MySQL DB Backup is Failed, WebPage Backup is OK!"
    subject = 'Gemside WebSite Backup Email'
    smtpserver = 'smtp.163.com'
    username = 'gemsidewebsite'
    password = 'gemside123456'
    content = "%s Please click link download backup files!\n\nDB Backup Download Address is: %s\nWebPage Backup Download Address is: %s\n\nMail from gemside website." % (backupinfo, db_dladdr, web_dladdr)
    msg = MIMEText(content, 'plain')
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def main():
    user = "root"
    password = "123456"
    dbname = "gemside"
    dbstatus, db_dladdr = mysqlBackup(user, password, dbname, backup_dir, today)
    webstatus, web_dladdr = webpageBackup(websource_dir, backup_dir, today)
    sendMail(mail_to_list, dbstatus, db_dladdr, webstatus, web_dladdr)

if __name__ == '__main__':
    main()
