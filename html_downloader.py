#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dell2014
# @Date:   2016-07-22 09:05:21
# @Last Modified by:   dell2014
# @Last Modified time: 2016-07-22 09:49:27

#下载器
import urllib2
from warnings import catch_warnings

class htmlDownloader(object):

	def download(self,url):
		if url is None:
			return None

		response = urllib2.urlopen(url)
		
		if response.getcode() != 200:
			return None
		return response.read()

