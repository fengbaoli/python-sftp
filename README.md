# python-sftp
Introduction

Scripts can be local files or folders through the SFTP to the remote Linux host, you can SFTP to a host or more

Getting started
1. git clone https://github.com/fengbaoli/python-sftp.git
2. Will require SFTP to remote files or folders to copy to the python-sftp directory
3.source python_env.sh
4.Edit file conf/hostname.txt file
Format as:
hostname:username:password
If you need to upload to multiple hosts, please add the above format to conf/hostname.txt
5.Edit sftp.py file
Parameter interpretation：
    remotepath = '/tmp'
    localpath = 'lib'
    
remotepath:for SFTP to remote directory
localpath:for SFTP local file or directory

6. python sftp.py

