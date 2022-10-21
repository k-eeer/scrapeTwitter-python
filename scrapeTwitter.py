import snscrape.modules.twitter as sntwitter
from datetime import datetime
import os,sys,mysql.connector

class UserScraper:
	def scrape():
		#使用者輸入欲搜尋的推特使用者名稱，生成該使用者最新三則推文的日期及url list
		user=f"from:{sys.argv[1]}"
		sntList=[]
		for i,tweet in enumerate(sntwitter.TwitterSearchScraper(user).get_items()):
			if i>2:
				break	
			sntDate=str(tweet.date.strftime("%Y-%m-%d"))
			sntList=sntList+[[sys.argv[1],sntDate,tweet.url]]
		return sntList
			
	
	def connectToMysql():
		#將scrape()中生成清單存入MySQL（表格內容限制為不可重複）
		mysqlName=f"{sys.argv[2]}"
		mysqlPwd=f"{sys.argv[3]}"
		
		mydb=mysql.connector.connect(user=mysqlName,password=mysqlPwd,host='127.0.0.1')
		mycursor=mydb.cursor()
		
		mycursor.execute("CREATE DATABASE IF NOT EXISTS twitter")
		mycursor.execute("USE Twitter")
		mycursor.execute("CREATE TABLE IF NOT EXISTS twitterPost(userName VARCHAR(50),postDate VARCHAR(50), postUrl VARCHAR(200),UNIQUE(postUrl))")
		sql = "INSERT INTO twitterPost(userName,postDate,PostUrl) VALUES (%s,%s,%s)"
		val=UserScraper.scrape()
		for i in val:
			try:
				mycursor.execute(sql, i)
			except:
				pass
		mydb.commit()

		#取出最新三則推文url以firefox新分頁打開
		mycursor.execute("SELECT * FROM twitterPost ORDER BY postDate DESC LIMIT 3")	
		myresult = mycursor.fetchall()
		for x in list(myresult):
			tabCommand=f"firefox --new-tab {x[2]}"
			os.system(tabCommand)						

UserScraper.connectToMysql()
