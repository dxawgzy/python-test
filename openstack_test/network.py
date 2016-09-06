#!/usr/bin/python

import json
import urllib2

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

def create(TOKEN,values,para):
    url = 'http://10.89.151.11:9696/v2.0/%s' %para+'s'
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------"
    for (k,v) in data2['%s'%para].items():
        print '%-20s  %-5s ' %(k, v)
    print "---------------------------------------------"
    para_id = data2['%s'%para]['id']
    return para_id

def add_interface_to_router(TOKEN,router_id,network_name,subnet_name,cidr_ip):
    values2 = {"network": {"name": network_name, "admin_state_up": True}}
    network_id = create(TOKEN,values2,'network')
    values3 = {"subnet": {"name": subnet_name, "network_id": network_id, "ip_version":4, "cidr": cidr_ip}}
    subnet_id = create(TOKEN,values3,'subnet')

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
    print "---------------------------------------------"
    for (k,v) in data2.items():
        print '%-15s  %-5s ' %(k, v)
    print "---------------------------------------------"

if __name__ == '__main__':
    TOKEN = get_token()
    #values1 = {"router": {"name": "gzytest_router", "admin_state_up": True}}
    values1 = {"router": {"name": "gzytest_router", "external_gateway_info": {"network_id": "5c9aadc3-ed0e-42a5-8ba5-71b5c957199c"}, "admin_state_up": True}}
    router_id = create(TOKEN,values1,'router')
    add_interface_to_router(TOKEN,router_id,'gzy_net1','gzy_subnet1','192.168.134.0/24')
    add_interface_to_router(TOKEN,router_id,'gzy_net2','gzy_subnet2','192.168.135.0/24')
    print 'successful!'

