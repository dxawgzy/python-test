#! /usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.letiantian.me/2015-09-10-understand-python-wsgi/?utm_source=tuicool&utm_medium=referral
__author__ = 'igis_gzy'

from wsgiref.simple_server import make_server
# cgi.parse_qs is deprecated, use urlparse.parse_qs instead
# from cgi import parse_qs, escape
from cgi import escape
from urlparse import parse_qs

html = """
<html>
<body>
   <form method="get" action="">
		<p>
		   Age: <input type="text" name="age" value="%(age)s">
		</p>
		<p>
			Hobbies:
			<input
				name="hobbies" type="checkbox" value="software"
				%(checked-software)s
			> Software
			<input
				name="hobbies" type="checkbox" value="tunning"
				%(checked-tunning)s
			> Auto Tunning
		</p>
		<p>
			<input type="submit" value="Submit">
		</p>
	</form>
	<p>
		Age: %(age)s<br>
		Hobbies: %(hobbies)s
	</p>
</body>
</html>
"""
def application (environ, start_response):
	# 解析QUERY_STRING
	d = parse_qs(environ['QUERY_STRING'])
	age = d.get('age', [''])[0]     # 返回age对应的值
	hobbies = d.get('hobbies', [])  # 以list形式返回所有的hobbies
	# 防止脚本注入
	age = escape(age)
	hobbies = [escape(hobby) for hobby in hobbies]
	response_body = html % {
		'checked-software': ('', 'checked')['software' in hobbies],
		'checked-tunning': ('', 'checked')['tunning' in hobbies],
		'age': age or 'Empty',
		'hobbies': ', '.join(hobbies or ['No Hobbies?'])
	}
	status = '200 OK'
	# 这次的content type是text/html
	response_headers = [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	]
	start_response(status, response_headers)
	return [response_body]
httpd = make_server('localhost', 8051, application)
# 能够一直处理请求
httpd.serve_forever()
print 'end'

