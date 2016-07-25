#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: dell2014
# @Date:   2016-07-22 09:05:35
# @Last Modified by:   dell2014
# @Last Modified time: 2016-07-22 10:12:36


class HtmlOutputer(object):

	def __init__(self):
		self.datas = []


	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)


	def output_html(self):
		fout = open("output.html",'w')

		#以html形式输出到文件
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")
		#python默认ascii，要转换成utf-8
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" %data['url'])
			fout.write("<td>%s</td>" %data['title'].encode('utf-8'))
			fout.write("<td>%s</td>" %data['summary'].encode('utf-8'))
			fout.write("</tr>")
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
