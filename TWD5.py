#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

#Import Twilio
from twilio.rest import Client
from datetime import datetime

account_sid = 'XXX'
auth_token = 'XXX'
twilio_phone_number = 'XXX'
my_phone_number = 'XXX'

client = Client(account_sid, auth_token)

# Following algorithm tries to install the library click if it hasn't already been installed.
try:
    import click
except:
    import os
    try:
        os.system("pip install click")
        import click
    except:
        try:
            os.system("C:\Python27\Scripts\pip install click")
            import click
        except:
            print("Please install the python library 'click' to run this program.")
            import sys
            sys.exit()


# Adds commandline argument using the click library and keeps the default value at 15 if nothing is specified.
@click.command()
@click.option('--count', default=15, help="number of times to run code.")
@click.option('--delay', default=30, help="seconds between each webpage check.")
def main(count, delay):
	while True:
		if (count == 0):
			break
		else:
			count -= 1
			job()
			time.sleep(delay)
#The code will run every 30 seconds, change this however you want
		



def job():
	
	page = requests.get("http://www.thinkgeek.com/product/khol/")
	soup = BeautifulSoup(page.content, 'html.parser')
	overall = soup.find(id = "product-actions")
	avail = overall.select("p.availability")
	print(avail[0].text)
	print datetime.now().strftime("%Y-%m-%d %H:%M")
	
#Printing the output to an out.txt file
	with open('out.txt', 'a') as f:
		f.write(avail[0].text)
		f.write(datetime.now().strftime("%Y-%m-%d %H:%M"))
		
#Text the information via Twilio
	body = name + ', ' + price + ', ' + str(datetime.now())
	client . messages.create(
		body=body,
		to=my_phone_number,
		from_=twilio_phone_number
		
if __name__ == '__main__':
    main()
