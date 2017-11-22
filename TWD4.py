#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

def job():
	page = requests.get("http://www.thinkgeek.com/product/khol/")
	soup = BeautifulSoup(page.content, 'html.parser')
	overall = soup.find(id = "product-actions")
	avail = overall.find('span', {'class':'in_stock'})
	print(avail.text)
	print datetime.now().strftime("%Y-%m-%d %H:%M")
	
	with open('out.txt', 'a') as f:
		f.write(avail.text)
		f.write(datetime.now().strftime("%Y-%m-%d %H:%M"))
		time.sleep(20)

if __name__ == '__main__':
	while True:
		job()
		time.sleep(20)


