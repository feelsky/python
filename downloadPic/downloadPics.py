from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import config

def downloadPic(filePath,fileName="de.jpg"):
    try:
        web = request.urlopen(filePath)
        print("要下载的图片:"+fileName)
        pic = web.read()
        picDir = config.localDir
        print("保存文件"+picDir+fileName+"\n")
        try:
            file = open(picDir+fileName,"wb")
            file.write(pic)
            file.close()
            return
        except IOError:
            print("IOerror\n")
            return
    except Exception:
        print("error\n")
        return

html = urlopen(config.webUrl)
bsObj = BeautifulSoup(html)

pics = bsObj.findAll("a",{"href":re.compile(config.picUrlRe)})
for pic in pics:
    #print(pic["href"])
    #print(pic.get_text())
    downloadPic(pic["href"],pic.get_text())
