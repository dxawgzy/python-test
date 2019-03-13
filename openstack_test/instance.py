#!/usr/bin/python

import json
import urllib2
import time

def get_token():
    url = 'http://10.89.151.11:35357/v2.0/tokens'
    values = {"auth":{"tenantName":"gzy","passwordCredentials":{"username":"gzy", "password": "123456"}}}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    data = response.read()
    text = json.loads(data)
    TOKEN = text['access']['token']['id']
    return TOKEN

def create_router_network_subnet(TOKEN,values,para):
    url = 'http://10.89.151.11:9696/v2.0/%s' %para+'s'
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------------------"
    for (k,v) in data2['%s'%para].items():
        print '%-20s  %-5s ' %(k, v)
    para_id = data2['%s'%para]['id']
    return para_id

def add_interface_to_router(TOKEN,router_id,subnet_id):
    url = 'http://10.89.151.11:9696/v2.0/routers/%s/add_router_interface' %router_id
    values ={"subnet_id": subnet_id}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'PUT'
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------------------"
    for (k,v) in data2.items():
        print '%-15s  %-5s ' %(k, v)

def remove_interface_from_router(TOKEN,router_id,subnet_id):
    url = 'http://10.89.151.11:9696/v2.0/routers/%s/remove_router_interface' %router_id
    values ={"subnet_id": subnet_id}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'PUT'
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------------------"
    for (k,v) in data2.items():
        print '%-15s  %-5s ' %(k, v)
    para_id = data2['port_id']
    return para_id

def delete_subnet_router_network(TOKEN,para,para_id):
    url = 'http://10.89.151.11:9696/v2.0/%s/%s' %(para+'s',para_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)


def create_volume(TOKEN,values,tenant_id,para):
    url = 'http://10.89.151.11:8776/v2/%s/%s' %(tenant_id,para+'s')
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------------------"
    for (k,v) in data2['%s'%para].items():
        print '%-20s  %-5s ' %(k, v)
    para_id = data2['%s'%para]['id']
    return para_id

def delete_volume(TOKEN,tenant_id,para,para_id):
    url = 'http://10.89.151.11:8776/v2/%s/%s/%s' %(tenant_id,para+'s',para_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)

def create_instance(TOKEN,values,tenant_id,para):
    url = 'http://10.89.151.11:8774/v2/%s/%s' %(tenant_id,para+'s')
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------------------"
    for (k,v) in data2['%s'%para].items():
        print '%-20s  %-5s ' %(k, v)
    para_id = data2['%s'%para]['id']
    return para_id

def delete_instance(TOKEN,tenant_id,para,para_id):
    url = 'http://10.89.151.11:8774/v2/%s/%s/%s' %(tenant_id,para+'s',para_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)

def instance_status(TOKEN,tenant_id,instance_id):
    url = 'http://10.89.151.11:8774/v2/%s/servers/%s' %(tenant_id,instance_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    """
    print "---------------------------------------------------------"
    for (k,v) in data2['server'].items():
        print '%-20s  %-5s ' %(k, v)
    """
    status = data2['server']['status']
    #if status != 'ACTIVE':
    return status


def attach_volume(TOKEN,values,tenant_id,instance_id):
    url = 'http://10.89.151.11:8774/v2/%s/servers/%s/os-volume_attachments' %(tenant_id,instance_id)
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------------------"
    for (k,v) in data2['volumeAttachment'].items():
        print '%-20s  %-5s ' %(k, v)

def detach_volume(TOKEN,tenant_id,instance_id,volume_id):
    url = 'http://10.89.151.11:8774/v2/%s/servers/%s/os-volume_attachments/%s' %(tenant_id,instance_id,volume_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)


if __name__ == '__main__':
    TOKEN = get_token()
    tenant_id = 'bd04a55a5b4c45b8b9d8891a2ce43555'
    values1 = {"router": {"name": "gzy_router1", "external_gateway_info":\
               {"network_id": "5c9aadc3-ed0e-42a5-8ba5-71b5c957199c"}, "admin_state_up": True}}
    router_id = create_router_network_subnet(TOKEN,values1,'router')
    values2 = {"python-network-programming": {"name": "gzy_net1", "admin_state_up": True}}
    network_id = create_router_network_subnet(TOKEN,values2,'python-network-programming')
    values3 = {"subnet": {"name": "gzy_subnet1", "network_id": network_id, "ip_version":4, "cidr": "192.168.134.0/24"}}
    subnet_id = create_router_network_subnet(TOKEN,values3,'subnet')
    add_interface_to_router(TOKEN,router_id,subnet_id)
    values4 = {"server": { "name": "gzy-instance", "imageRef": "27514db1-a43d-4663-97ba-bfae76864c98",\
               "flavorRef": "424f759f-6bde-48ba-bcca-62bfa4eef8e9", "networks": [{"uuid": network_id}]}}
    instance_id = create_instance(TOKEN,values4,tenant_id,'server')
    time.sleep(15)
    status = instance_status(TOKEN,tenant_id,instance_id)
    print status
    if status == 'ACTIVE':
        values5 = {"volume": {"size": 1, "volume_type": "macrosan_iscsi", "name": "gzy-volume"}}
        volume_id = create_volume(TOKEN,values5,tenant_id,'volume')
        time.sleep(15)
        values6 = {"volumeAttachment": {"volumeId": volume_id , "device": "/dev/vdb"}}
        attach_volume(TOKEN,values6,tenant_id,instance_id)

    """
    detach_volume(TOKEN,tenant_id,instance_id,volume_id)
    delete_volume(TOKEN,tenant_id,'volume',volume_id)
    delete_instance(TOKEN,tenant_id,'server',instance_id)
    remove_interface_from_router(TOKEN,router_id,subnet_id)
    time.sleep(3)
    delete_subnet_router_network(TOKEN,'router',router_id)
    delete_subnet_router_network(TOKEN,'subnet',subnet_id)
    delete_subnet_router_network(TOKEN,'python-network-programming',network_id)
    """



