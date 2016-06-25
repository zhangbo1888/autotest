#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time
import sys
sys.path.append("..")
from Common import *
import Common.conlogs
import web
import logging
import datetime
PASS=0
FAIL=0

#默认得安装一个火狐浏览器
class webconn:

	def web_conn(self):  
		global PASS
		global FAIL
		starttime=datetime.datetime.now()
		driver = webdriver.Firefox()

		try:

			logging.info("open firefox driver")
			driver.get('http://www.python.org')
			logging.info("open pythonorg homepage")
			time.sleep(3)
			assert 'Python' in driver.title
			logging.info("if the driver title has the word 'Python'")
			elem = driver.find_element_by_name('q')
			logging.info("fined element by name 'q'")	
			elem.send_keys('pycon')
			logging.info("insert pycon")
			elem.send_keys(Keys.RETURN)
			logging.info("enter")
			assert 'No results found.' not in driver.page_source
			logging.info("make sure there is no 'No results found'")
			logging.info("success")
			PASS=PASS+1
		except Exception,e:
			logging.error(str(Exception)+":"+str(e))
			FAIL=FAIL+1
		finally:
			driver.close()

		endtime=datetime.datetime.now()
		totaltime=endtime-starttime
		usetime=str(endtime-starttime)
		hour=usetime.split(':').pop(0)
		minute=usetime.split(':').pop(1)
		second=usetime.split(':').pop(2)
		totaltime=float(hour)*60*60+float(minute)*60+float(second)
		totaltime=str(totaltime)+"s"
		return (totaltime,PASS,FAIL)

if __name__=="__main__":
	con=webconn()
	result=con.web_conn()
	# logging.info(result[0])
	# logging.info(result[1])
	# logging.info(result[2])
	print result[0]
	print result[1]
	print result[2]

