#coding=utf-8
#!usr/bin/python  #P177
import sys, email

msg = email.message_from_file(sys.stdin)

print " *** Headers message: "
for header, value in msg.items():
#for header, value in msg.keys(): #不能使用keys, 因为有两个key为Received，items则是遍历输出
    print header + ":"
#for key, value in msg.items():
#    print key + ":"
    print " " + value

if msg.is_multipart():
    print "This program cannot handle MIME multipart messages; exiting."
    sys.exit(1)
print "-" *60

if 'subject' in msg:
    print "Subject: ", msg['subject']
    print "-" * 60
print "Message Body:"
print msg.get_payload()

#python message.py < message.txt
"""
 *** Headers message:
Received:
 By test server from somewhere
Received:
 By another server from my machine
To:
 recipient@example.com
From:
 Test Sender <sender@example.com>
Subject:
 Test Message, Chapter 9
Date:
 Tue, 09 Dec 2003 15:29:18 -0600
Message-ID:
 <20031209212918.10574.60752@somewhere.com>
------------------------------------------------------------
Subject:  Test Message, Chapter 9
------------------------------------------------------------
Message Body:
Hello,

This is a test message from Chapter 9. I hope you enjoy it.

-- Anonymous

"""

