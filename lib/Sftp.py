# -*- coding: utf-8 -*-
__author__ = 'blfeng'


import  os,Sftp,string


def VisitDir(hostname,port,password,username,path,remotepath):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        if not  os.path.isfile(pathname):
            VisitDir(hostname=hostname,port=port,username=username,password=password,path=pathname,remotepath=remotepath)
        else:
            x = Sftp.Sftp()
            x.sftp(hostname=hostname,port=port,password=password,username=username,localpath=pathname,remotepath=remotepath)



f=open("conf/hostname.txt")
while True:
    line = f.readline()
    if line:
        ini_line = line.split(':',3)
        c = map(string.strip, ini_line)
        hostname = c[0]
        username = c[1]
        password = c[2]
        port = 22
        path = os.path.abspath('.')+"/gernerRSAkey"
        remotepath='/tmp/gg'
        VisitDir(hostname=hostname,port=port,password=password,username=username,path=path,remotepath=remotepath)
    else:
        break
