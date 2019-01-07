#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import requests

r = requests.head("http://httpbin.org/headers")
print r.headers

