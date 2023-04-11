import twint,os,webbrowser
from datetime import datetime
def scrapeByUserName():
	if os.path.exists('tweet.log'):os.remove('tweet.log')
	c = twint.Config()
	c.Username = input("please input target user name\n")
	c.Output = "tweet.log"
	c.Limit=1
	c.Hide_output=True
	c.Format="{name}|{date}|{link}"
	twint.run.Search(c)
def readUrlAndOpenNewTab():
	with open("tweet.log") as file:
		data=file.readlines()[-3:]
	for i in data:
		webbrowser.open_new_tab(list(i.split('|'))[2])
if __name__=='__main__':
	scrapeByUserName()
	readUrlAndOpenNewTab()




	
