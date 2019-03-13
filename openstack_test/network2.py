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
    if para == 'router':
        for (k,v) in data2['%s'%para].items():
            print '%-16s  %-5s ' %(k, v)
        para_id = data2['%s'%para]['id']
        return para_id
    else:
        data3s = data2['%s'%para+'s']
        for data3 in data3s:
            for (k,v) in data3.items():
                print '%-16s  %-5s ' %(k, v)
            print "---------------------------------------------"
        para_ids = []
        for i in range(len(data3s)):
            para_ids.append(data3s[i]['id'])
        return para_ids

def create_network_subnet(TOKEN):
    values2 = {"networks": [{"name": "gzy_net1", "admin_state_up": True}, {"name": "gzy_net2", "admin_state_up": True}]}
    network_ids = create(TOKEN,values2,'python-network-programming')
    values3 = {"subnets": [{"name": "gzy_subnet1", "network_id": network_ids[0], "ip_version":4, "cidr": "192.168.134.0/24"},\
                           {"name": "gzy_subnet2", "network_id": network_ids[1], "ip_version":4, "cidr": "192.168.135.0/24"}]}
    subnet_ids = create(TOKEN,values3,'subnet')
    return subnet_ids

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
    print "---------------------------------------------"
    for (k,v) in data2.items():
        print '%-16s  %-5s ' %(k, v)

if __name__ == '__main__':
    TOKEN = get_token()
    values1 = {"router": {"name": "gzytest_router", "external_gateway_info": {"network_id": "5c9aadc3-ed0e-42a5-8ba5-71b5c957199c"}, "admin_state_up": True}}
    router_id = create(TOKEN,values1,'router')
    subnet_ids = create_network_subnet(TOKEN)
    add_interface_to_router(TOKEN,router_id,subnet_ids[0])
    add_interface_to_router(TOKEN,router_id,subnet_ids[1])
    print 'successful!'

