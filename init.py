import requests 
import csv
from datetime import datetime
from bs4 import BeautifulSoup


today = datetime.now().strftime("%Y%m%d%H%M%S")
print(today)

f = open('searchList.csv', 'r', encoding='utf-8')
w = open(today+'.csv','w',encoding='utf-8')

reader = csv.reader(f)
writer = csv.writer(w)
items = []

for line in reader:
    for elem in line:
        items.append(elem.strip())

output = []
for i in items:
    arr = [i]
    q = i.replace(' ','%20').replace('　','%20')
    url = 'https://kakaku.com/search_results/'+q
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find('title')
    name = soup.select('#default > div.l-c.l-c-2column.l-c-2column-reverse > div.l-c_cont.l-c-2column_cont.p-cont.p-cont-wide > div > div.p-result_list_wrap > div > div:nth-child(1) > div > div.c-positioning_cell.p-result_item_cell-1 > div.c-positioning.s-biggerlink.is-biggerlinkHot.p-item > div > p.p-item_name.s-biggerlinkHover_underline')
    price =  soup.select('#default > div.l-c.l-c-2column.l-c-2column-reverse > div.l-c_cont.l-c-2column_cont.p-cont.p-cont-wide > div > div.p-result_list_wrap > div > div:nth-child(1) > div > div.c-positioning_cell.p-result_item_cell-2 > div > p.p-item_price > span')
    if len(name)>0 and len(price)>0:
        arr.append(name[0].text)
        arr.append(price[0].text)
        arr.append(url)

    output.append(arr)

writer.writerows(output)
print(output)