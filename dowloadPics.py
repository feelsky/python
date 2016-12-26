from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib import request

def downloadPic(filePath,fileName="de.jpg"):
    try:
        web = request.urlopen(filePath)
        print("要下载的图片:"+fileName)
        pic = web.read()
        picDir = "F:\\pics\\"
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

html = urlopen("http://docs.heweather.com/224292")
bsObj = BeautifulSoup(html)

pics = bsObj.findAll("a",{"href":re.compile("http\:\/\/files\.heweather\.com\/.*\.png")})
for pic in pics:
    #print(pic["href"])
    #print(pic.get_text())
    downloadPic(pic["href"],pic.get_text())

