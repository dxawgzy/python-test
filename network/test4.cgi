#!usr/bin/python

import cgitb
cgitb.enable()

import time
print "Content-type: text/html"

print """<HTML>
<HEAD>
<TITLE>Sample CGI Script</TITLE>
</HEAD>
<BODY>
The present time is %s.
</BODY>
</HTML>""" % time.strftime("%I:%M:%S %p %Z")
print





