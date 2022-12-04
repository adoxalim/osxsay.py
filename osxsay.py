from bs4 import BeautifulSoup
import requests
import os
import time
import sys
import os
def cmdtodata(data):
    data = sys.stdin.readline()
    return data
websitetoread=input("Insert any website you want to listen.:")
sitedata = requests.get(websitetoread)
soup=BeautifulSoup(sitedata.text,"html.parser")
dil="say -v'?' | grep "+websitetoread.split("//")[1][0:2]+"_"
cmdoutput=os.popen(dil).read()
speaker=(cmdoutput.split(" ")[0])
singlequote={39:32}
doublequote={34:32}
for paragraph in soup.find_all("p"):
    print(dil)
    if dil=="say -v'?' | grep en_":
        texttoread = str(paragraph.get_text()).translate(singlequote).translate(doublequote)
        shell="say \'"+texttoread+"\'"
    else:
        texttoread = str(paragraph.get_text()).translate(singlequote).translate(doublequote)
        shell="say -v "+speaker+" \'"+texttoread+"\'"
    os.system(shell)
    time.sleep(1)
