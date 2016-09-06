#!/usr/bin/python

import json
import urllib2

def get_token():
    url = 'http://192.168.1.11:5000/v2.0/tokens'
    values = {"auth":{"tenantName":"admin","passwordCredentials":{"username":"admin", "password": "Abc12345"}}}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    data = response.read()
    #print data
    text = json.loads(data)
    TOKEN = text['access']['token']['id']
    return TOKEN
    #print TOKEN

def list():
    TOKEN = get_token()
    url = 'http://192.168.1.11:35357/v2.0/users'
    #values = {"auth":{"X-Auth-token":"TOKEN"}}
    #params = json.dumps(values)
    #headers = {"X-Auth_token":"TOKEN","Content-type":"application/json","Accept": "application/json"}
    #headers = {"Content-type":"application/json","Accept": "application/json"}
    #req = urllib2.Request(url, params ,headers)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    #print data
    data2 = json.loads(data)
    #print data2
    user2s = data2['users']
    #print user2s
    for user2 in user2s:
        userlist = user2['name']
        print userlist

if __name__ == '__main__':
    list()



