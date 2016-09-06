#!usr/bin/python  #P358

import xmlrpclib, code

url = 'http://localhost:8765'
s = xmlrpclib.ServerProxy(url)

interp = code.InteractiveConsole({'s':s})
interp.interact("You can now use the object s to interact with the server.")


"""
First run simplexmlrpc.py (P356),then run:
D:\workspace\selenium\python-network>python simplexmlrpctestclient.py
You can now use the object s to interact with the server.
>>> s.pow(2, 8)
256
>>> s.hex(255)
'ff'
>>> s.system.listMethods()
['hex', 'pow', 'system.listMethods', 'system.methodHelp', 'system.methodSignature']
>>>
>>> print s.system.methodHelp('pow')
Return x raised to the yth power; that is, x ** y.
x and y may be integers or floating-point values.
>>> sys.exit()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'sys' is not defined

"""


