#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

#!/usr/bin/env python
import logging
import novaclient
# from novaclient.v2 import client
from novaclient import client

# enable debug logging
logger = logging.getLogger('novaclient.client')
logger.setLevel(logging.DEBUG)
debug_stream = logging.StreamHandler()
logger.addHandler(debug_stream)

#auth_url = 'http://10.100.20.22:5000/v2.0'
auth_url = 'http://192.168.251.30:35357/v3'
user = 'admin'
password = '123456'
project = 'admin'
region = 'RegionOne'
service = 'compute'
version = '2.0'

# nova = client.Client(user, password, project, auth_url,
nova = client.Client(version=version, username=user, password=password, project_name=project, auth_url=auth_url,
                     region_name=region, service_type=service)

results = nova.images.list(detailed=True)
for image in results:

    print image.id, image.name, image.status
