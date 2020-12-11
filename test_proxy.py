#!/usr/bin/env python
# coding: utf-8
"""
代理IP池实例演示
"""
from __future__ import print_function

import time
import requests

while True:
	s = requests.Session()
	s.proxies.update({"http": "127.0.0.1:16889"})
	print(s.get("http://httpbin.org/ip").content)
	time.sleep(1)
