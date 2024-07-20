
# ..............web scrapping............
# import requests
# print(dir(requests))
# # # # # #Right click and  run...
# response=requests.get("https://opensource.com/article/21/9/web-scraping-python-beautiful-soup")
# print(response.status_code)
# # # #Right click and  run...
# # # #scrap the image
# response=requests.get("https://opensource.com/sites/default/files/lead-images/browser_screen_windows_files.png")
# img=response.content
# f=open("image.png","wb")
# f.write(img)
#....run....
#................Beautiful soup..............
import requests
from bs4 import BeautifulSoup as bs
import lxml
# # # # #
response = requests.get("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area")
print(response.status_code)
# # # # # # ..run..
res=response.text
soup=bs(res,'lxml')
sp=soup.prettify()
print(sp)
# # # # # #...run....
table = soup.find('table',{'class':"sortable"})
print(table)
# # # # # # #..run..
link = table.findAll('a')
a=[]
#
for i in link:
    j=i.get('title')
    a.append(j)
print(a)
# # # # #...run..
import pandas as pd
data = pd.DataFrame()
data['country']=a
data.to_csv('list.csv')
# # #..run...
#

