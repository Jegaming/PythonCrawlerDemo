#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dell2014
# @Date:   2016-07-22 09:04:50
# @Last Modified by:   dell2014
# @Last Modified time: 2016-07-22 10:24:14
from myCrawler import url_manager, html_downloader, html_parser, html_outputer

 
#爬虫总调度
class SpiderMain(object):
	
	
	def __init__(self):
		self.urls = url_manager.UrlManager()				#url管理器
		self.downloader = html_downloader.htmlDownloader()	#html下载器
		self.parser = html_parser.HtmlParser()				#html解析器
		self.outputer = html_outputer.HtmlOutputer()		#网页输出器

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():#判断是否有未下载的url
			try:
				#取出URL
				new_url = self.urls.get_new_url()
				print 'craw %d : %s' %(count , new_url)
				#下载页面
				html_cont = self.downloader.download(new_url)
				#解析页面
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				#url添加进url管理器
				self.urls.add_new_urls(new_urls)
				#收集数据
				self.outputer.collect_data(new_data)
				count = count+1
				if count == 100:
					break
			except:
				print "craw failed"
		
		#手机数据
		self.outputer.output_html()
		print 'task success '



if __name__ == "__main__":
	#入口URL
	root_url = "http://baike.baidu.com/view/10688863.htm"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
