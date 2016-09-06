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

def create_project(TOKEN,project_name):
    url = 'http://10.89.151.11:35357/v3/projects'
    values ={"project": {"description": "My test project", "domain_id": "default", "enabled": True, "is_domain": True, "name": project_name}}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    print "---------------------------------------------"
    for (k,v) in data2['project'].items():
        print '%-20s  %-5s ' %(k, v)
    print "---------------------------------------------"
    project_id = data2['project']['id']
    return project_id

def create_role(TOKEN,role_name):
    url = 'http://10.89.151.11:35357/v3/roles'
    values ={"role": {"name": role_name}}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    for (k,v) in data2['role'].items():
        print '%-20s  %-5s ' %(k, v)
    print "---------------------------------------------"
    role_id = data2['role']['id']
    return role_id

def create_user(TOKEN,user_name,project_id):
    url = 'http://10.89.151.11:35357/v3/users'
    values ={"user": {"default_project_id": project_id, "description": "My test user", "name": user_name, "password": "123456"}}
    params = json.dumps(values)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    data = response.read()
    data2 = json.loads(data)
    for (k,v) in data2['user'].items():
        print '%-20s  %-5s ' %(k, v)
    print "---------------------------------------------"
    user_id = data2['user']['id']
    return user_id

def grant_role_to_user(TOKEN,user_name,role_name,project_name):
    project_id = create_project(TOKEN,sys.argv[4])
    role_id = create_role(TOKEN,sys.argv[3])
    user_id = create_user(TOKEN,sys.argv[2],project_id)
    url = 'http://10.89.151.11:35357/v3/projects/%s/users/%s/roles/%s' %(project_id,user_id,role_id)
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'PUT'
    response = urllib2.urlopen(req)


def delete_project(TOKEN,project_name): 
    url = 'http://10.89.151.11:35357/v3/projects'
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    projectdata = response.read()
    projectdata2 = json.loads(projectdata)
    project2s = projectdata2['projects']
    for project2 in project2s:
        if project2['name'] == project_name:
            project_id = project2['id']
    url = 'http://10.89.151.11:35357/v3/projects/%s' %project_id
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)

def delete_role(TOKEN,role_name):
    url = 'http://10.89.151.11:35357/v3/roles'
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    roledata = response.read()
    roledata2 = json.loads(roledata)
    role2s = roledata2['roles']
    for role2 in role2s:
        if role2['name'] == role_name:
            role_id = role2['id']
    url = 'http://10.89.151.11:35357/v3/roles/%s' %role_id
    req = urllib2.Request(url)
    req.get_method = lambda: 'DELETE'
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)

def delete_user(TOKEN,user_name):
    url = 'http://10.89.151.11:35357/v3/users'
    req = urllib2.Request(url)
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)
    userdata = response.read()
    userdata2 = json.loads(userdata)
    user2s = userdata2['users']
    for user2 in user2s:
        if user2['name'] == user_name:
            user_id = user2['id']
    url = 'http://10.89.151.11:35357/v3/users/%s' %user_id
    req = urllib2.Request(url)
    req.get_method = lambda: 'DELETE'
    req.add_header("X-Auth-token",TOKEN)
    response = urllib2.urlopen(req)

def delete_project_role_user(TOKEN,user_name,role_name,project_name):
    delete_user(TOKEN,sys.argv[2])
    delete_role(TOKEN,sys.argv[3])
    delete_project(TOKEN,sys.argv[4])
    print "delete success!"


if __name__ == '__main__':
    TOKEN = get_token()
    option = sys.argv[1][1:]
    if len(sys.argv)!=5:
        print 'The number of input parameters is error !'
        sys.exit(1)
    elif option == 'a':
        grant_role_to_user(TOKEN,sys.argv[2],sys.argv[3],sys.argv[4])
    elif option == 'd':
        delete_project_role_user(TOKEN,sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        print 'Unknown option.'






