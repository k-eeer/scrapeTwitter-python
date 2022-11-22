import snscrape.modules.twitter as sntwitter
from datetime import datetime
import os,sys,mysql.connector
from scrape import Scraper 

def test_user_scrape():	
	
	#arrange:準備變數值
	expected=sys.argv[2]
	result_list=[]

	#act:執行待測部份
	result_list=(Scraper.userScrape())	
	#assert:確認結果是否符合預期
	for element in result_list:
		result=(element[2].split('/'))[3]
		assert result==expected
