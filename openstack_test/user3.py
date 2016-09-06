#!/usr/bin/python

import json
import urllib2
import sys

def get_token():
    url = 'http://10.89.151.11:35357/v2.0/tokens'
    values = {"auth":{"tenantName":"admin","passwordCredentials":{"username":"admin", "password": "Abc12345"}}}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    data = response.read()
    text = json.loads(data)
    TOKEN = text['access']['token']['id']
    return TOKEN

def create(TOKEN,values,para):
    url = 'http://10.89.151.11:35357/v3/%s' %para+'s'
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

def grant_role_to_user(TOKEN,user_name,role_name,project_name):
    try:
        values1 ={"project": {"description": "My test project", "domain_id": "default", "enabled": True, "is_domain": True, "name": sys.argv[4]}}
        project_id = create(TOKEN,values1,'project')
        values2 ={"role": {"name": sys.argv[3]}}
        role_id = create(TOKEN,values2,'role')
        values3 ={"user": {"default_project_id": project_id, "description": "My test user", "name": sys.argv[2], "password": "123456"}}
        user_id = create(TOKEN,values3,'user')
        url = 'http://10.89.151.11:35357/v3/projects/%s/users/%s/roles/%s' %(project_id,user_id,role_id)
        req = urllib2.Request(url)
        req.add_header("X-Auth-token",TOKEN)
        req.get_method = lambda: 'PUT'
        response = urllib2.urlopen(req)
    except:
        print 'Error: What you want to add is existed!'

def delete(TOKEN,para,para_name): 
    url = 'http://10.89.151.11:35357/v3/%s'%para
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    datalist2s = data2['%s'%para]
    for datalist2 in datalist2s:
        if datalist2['name'] == para_name:
            para_id = datalist2['id']
    url = 'http://10.89.151.11:35357/v3/%s/%s' %(para,para_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)

def delete_project_role_user(TOKEN,user_name,role_name,project_name):
    try:
        delete(TOKEN,'users',sys.argv[2])
        delete(TOKEN,'roles',sys.argv[3])
        delete(TOKEN,'projects',sys.argv[4])
        print "delete success!"
    except:
        print 'Error: What you want to delete is not existed!'

if __name__ == '__main__':
    TOKEN = get_token()
    option = sys.argv[1][1:]
    if len(sys.argv)!=5:
        print 'The number of input parameters is error !'
        sys.exit()
    elif option == 'a':
        grant_role_to_user(TOKEN,sys.argv[2],sys.argv[3],sys.argv[4])
    elif option == 'd':
        delete_project_role_user(TOKEN,sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        print 'Unknown option.'






