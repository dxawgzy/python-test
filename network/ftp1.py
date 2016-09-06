#!usr/bin/python  #278
from ftplib import FTP

def writeline(data):
    fd.write(data + "\n")

f = FTP('ftp.kernel.org')
#f = FTP('ftp.openssl.org')
#print "Welcome: ", f.getwelcome()
f.login()

f.cwd('/pub/linux/kernel')
#f.cwd('/source')
fd = open('README', 'wt')
f.retrlines('RETR README', writeline)
fd.close()
f.quit()



