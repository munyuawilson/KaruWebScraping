#scrap the notice board of karu

from bs4 import BeautifulSoup
import requests
import lxml
url="https://karu.ac.ke/student-notice-board/"
get=requests.get(url,verify=False).text
content=BeautifulSoup(get,'html.parser')
All_div=content.find('div',class_="gdlr-core-pbf-column gdlr-core-column-60 gdlr-core-column-first")

ntitles=All_div.find_all('h3',class_="gdlr-core-blog-title gdlr-core-skin-title")
for n in ntitles:
    notices=n.a.text.strip()
    
    with open('notice.txt',"a") as file:
        file.write(notices+'\n')
        file.close()
    print(notices)
        
