#!/usr/bin/env python
__author__ = 'igis_gzy'

from oslo_vmware import api
from oslo_vmware import vim_util

# Get a handle to a vSphere API session
session = api.VMwareAPISession(
    '192.168.126.2',   # vCenter_IP
    'root',            # vCenter_username
    'vmware',          # vCenter_password
    1,
    0.1)

# Get MO of type "HostSystem"
result1 = session.invoke_api(
    vim_util,
    'get_objects',
    session.vim, 'HostSystem', 100)
print "="*50
print result1
print "="*50

# Get information by properties of MO object
rep2 = session.invoke_api(vim_util,'get_object_properties_dict',session.vim,
result1.objects[0].obj,'vm')
print "*"*50
print rep2
print "*"*50

rep3 = session.invoke_api(vim_util,'get_object_properties_dict',session.vim,
rep2['vm'].ManagedObjectReference[0],'summary')
print "="*50
print rep3
print "="*50

rep4 = session.invoke_api(vim_util,'get_object_properties_dict',session.vim,
rep3['summary'][0],'config')
print "*"*50
print rep4
print "*"*50

