#coding=utf-8
#!/usr/bin/python  #P212
import sys, getpass, poplib

(host, user) = sys.argv[1:]
passwd = getpass.getpass()
p = poplib.POP3(host)
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto, e:
    print "Login failed:", e
    sys.exit(1)
status = p.stat()
"""def stat(self): Get mailbox status.
   Result is tuple of 2 ints (message count, mailbox size)
"""
print "Mailbox has %d message for a total of %d bytes" % (status[0], status[1])

"""
#list()返回一个包含两个条目的tuple，应答代码和字符串列表list。
#list中每一个字符串包含两个条目，邮件数字和字节数，两者之间有一个空格，使用split()得到每部分。
for item in p.list()[1]:
    number, octets = item.split(' ')
    print "Message %s: %s bytes" % (number, octets)
"""

p.quit()


#python pop1.py mail username
"""
Password:
Mailbox has 146 message for a total of 82960776 bytes
"""


