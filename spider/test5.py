#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

import requests

r = requests.get('https://github.com', verify=True)
print r.text

