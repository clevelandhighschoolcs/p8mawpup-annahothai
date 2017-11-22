#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

#The count sets how many times to run the code
count = 15

def job():
	
	page = requests.get("http://www.thinkgeek.com/product/khol/")
	soup = BeautifulSoup(page.content, 'html.parser')
	overall = soup.find(id = "product-actions")
	avail = overall.find('span', {'class':'in_stock'})
	print(avail.text)
	print datetime.now().strftime("%Y-%m-%d %H:%M")
	
#Printing the output to an out.txt file
	with open('out.txt', 'a') as f:
		f.write(avail.text)
		f.write(datetime.now().strftime("%Y-%m-%d %H:%M"))
		
if __name__ == '__main__':
	while True:
		if (count == 0):
			break
		else:
			count -= 1
			job()
			time.sleep(30)
#The code will run every 30 seconds, change this however you want
		
