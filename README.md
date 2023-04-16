# scrapeTwitter-python-描述及用法:
面對關心及更新較快的用戶更新內容，可以以此工具快速觀看推文回覆或是使用推文翻譯功能。
此腳本將搜尋特定推特用戶名的三則最新推文，儲存至log文字檔，並以預設瀏覽器分頁分別自動開啟此三則推文。無須登入
    
    $echo <username>|python scrape.py 例如 $echo TIME|python scrape.py
    或
    $python scrape.py之後，待出現詢問句，再輸入<username>+enter

# 運行環境:
  * Ubuntu 20.04 
  * twint 2.1.20
  * python 3.10.6


# 其他建議:

  * 避免"error twint requires python version 3.6+" [https://github.com/twintproject/twint/issues/1346#issuecomment-1062456345](https://github.com/twintproject/twint/issues/1346#issuecomment-1062456345)
  * 避免 token 相關error,應將原本 $HOME/.local/lib/python3.10/site-packages/twint中cli.py更換成此版本
  [https://gist.github.com/moxak/ed83dd4169112a0b1669500fe855101a](https://gist.github.com/moxak/ed83dd4169112a0b1669500fe855101a)
  * 避免"......user is suspend......"[https://github.com/twintproject/twint/issues/1003#issuecomment-721572595](https://github.com/twintproject/twint/issues/1003#issuecomment-721572595)
  * 避免"c.Format TypeError: replace() argument 2 must be str, not int" 應修改 $HOME/.local/lib/python3.10/site-packages/twint/format.py [https://github.com/twintproject/twint/issues/1232#issuecomment-873643082](https://github.com/twintproject/twint/issues/1232#issuecomment-873643082)


# 實際結果:

![image](https://github.com/k-eeer/scrapeTwitter-python/blob/main/scrapeDemo.png)

使用者輸入用戶名後將自動打開三則最新推文的瀏覽器分頁，本次使用url可參考新產生的tweet.log

若使用echo 提前輸入選擇，可略過此行，等待瀏覽器自動打開分頁












