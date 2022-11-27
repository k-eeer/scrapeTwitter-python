import snscrape.modules.twitter as sntwitter
from datetime import datetime
import os,sys,mysql.connector
from scrape import Scraper 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_user_scrape():#由得到的URL確定用戶名是否正確
	
	#arrange:準備變數值
	expected=sys.argv[2]
	result_list=[]

	#act:執行待測部份
	result_list=(Scraper.userScrape())	
	
	#assert:確認結果是否符合預期
	for element in result_list:
		result=(element[2].split('/'))[3]
		assert result==expected

def test_url_and_date():#檢視MySQL中url所配對的推文日期是否正確
		
	#arrange:
	mysqlName=f"{sys.argv[3]}"
	mysqlPwd=f"{sys.argv[4]}"
	mydb=mysql.connector.connect(user=mysqlName,password=mysqlPwd,host='127.0.0.1',database='Twitter')
	mycursor=mydb.cursor()
	mycursor.execute("SELECT * FROM twitterPost ORDER BY postDate DESC LIMIT 3")
	myresult = mycursor.fetchall()
	#expected=[list[0] for list in myresult]
	
	#act:
	for x in list(myresult):
		driver=webdriver.Firefox()
		driver.get(x[2])
		expected=(x[1])
		time.sleep(6)
		a=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[3]/div[5]/div/div[1]/div/a[1]/time")
	#assert:
		result=((a.get_attribute('datetime')).split('T'))[0]
		assert result==expected
