*This is a work for my school computer science assignment*
Here is the code for my webscraping mini project. I decided to go to Thinkgeek, an awesome geeky nerdy merchandise website that has super cool stuffs that drain my wallet. Ironically, I decided to keep track of this product http://www.thinkgeek.com/product/khol/. That's right, The official cookbook based on The Walking Dead. Because who doesn't want to know Carol's secret cookie recipe? (applesauce is her secret ingredient wink wink). 
For the code, I'm keeping track of the availability status, whether it's still "In Stock" or not. Because who knows, one day I might decide to buy this book unironically and I'd need to know if the book's still available.

Enough blah blah, here's the instruction on how to install it:

*Created and compatible with Python version 2.7.8

#**Instruction**

1. Open the command prompt and install Beautifulsoup via pip:
 
- ```easy_install pip```
   
   Or follow the instruction to install pip on this link: https://pip.pypa.io/en/stable/installing/
- ```pip install beautifulsoup4```
(if all else failed and you can't install Beautifulsoup, try downloading directly from https://www.crummy.com/software/BeautifulSoup/)

2. Install the Requests library
    ```pip install requests```
    
3. Create and activate a virtual environment you want to run the code in

```
cd C:\Python27\Scripts
pip install virtualenv
cd C:\Users\"Username"\Documents\
mkdir Python
cd Python
C:\Python27\Scripts\virtualenv.exe -p C:\Python27\python.exe
.lpvenv\Scripts\activate
```

4. Download TWD5.py or copy the code and paste it to your notepad++ file (make sure to name your file with .py extension)

5. Run TWD5.py by typing in \Yourfilelocation\TWD5.py(or whatever you renamed your file) in your virtual environment

4. A status read "In Stock" or otherwise and the date and time should appear on the screen

5. I also made the results print out as a text file so that you can see the comparison. Search for an "out.txt" file on your computer and you should see the availibility status and the date printed on simple notepad file.  


**Resources**
*Here is a list of sources I came across while working on the project*
- https://chrisalbon.com/python/monitor_a_website.html
- https://gist.github.com/bradmontgomery/1872970
- http://docs.python-guide.org/en/latest/scenarios/scrape/
- http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/
- https://stackoverflow.com/questions/39510830/extract-data-from-website-using-python
- https://journalistsresource.org/tip-sheets/research/python-scrape-website-data-criminal-justice
- https://www.dataquest.io/blog/web-scraping-tutorial-python/

Also, here was my first nice stupid idea for website to monitor
http://hasthelargehadroncolliderdestroyedtheworldyet.com/
