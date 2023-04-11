import twint,os,webbrowser
from datetime import datetime
def scrapeByUserName():
	'''以Username搜尋該使用者最近20則推文，
	並將其名字、推文日期、推文連結存入tweet.log'''
	if os.path.exists('tweet.log'):os.remove('tweet.log')
	c = twint.Config()
	c.Username = input("please input target user name\n")
	c.Output = "tweet.log"
	c.Limit=1
	c.Hide_output=True
	c.Format="{name}|{date} {time}|{link}"
	twint.run.Search(c)

def readUrlAndOpenNewTab():
	'''將最近三則推文各自以瀏覽器新分頁開啟'''
	with open("tweet.log") as file:
		data=file.readlines()[0:3]
	for i in data:
		webbrowser.open_new_tab(list(i.split('|'))[2])
if __name__=='__main__':
	scrapeByUserName()
	readUrlAndOpenNewTab()

