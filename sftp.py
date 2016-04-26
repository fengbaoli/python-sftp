# -*- coding: utf-8 -*-
__author__ = 'blfeng'
import  paramiko,os,Sftp,string

def main():
    hostname = ''
    username = ''
    password = ''
    remotepath = '/tmp'
    localpath = 'lib'
    port = 22
    f=open("conf/hostname.txt")
    while True:
        line = f.readline()
        if line:
            ini_line = line.split(':',3)
            c = map(string.strip, ini_line)
            hostname=c[0]
            username=c[1]
            password=c[2]
            s = Sftp.Sftp(hostname=hostname,username=username,password= password,port=port,localpath=localpath,remotepath=remotepath)
            s.sftp()
            
        else:
            break

if __name__=='__main__':
    main()
