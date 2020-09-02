from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#open connection, grab page
my_url = "http://www.dailymail.co.uk/sciencetech/index.html"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parse
page_soup = soup(page_html, 'lxml')

#Search for a keyword in an article
keyword = "bronze"

#Grabs each article
main_containers = page_soup.findAll("div", {"class":"article article-tri-headline"})
small_containers = page_soup.findAll("div", {"class":"article article-small"})

#grabs each article title
for contain in main_containers:

	title_container = contain.findAll("h2", {"class":"linkro-darkred"})
	href = str(contain.a)

	#prints the URL and title if any results are found
	if keyword in href.lower():
		itemprop = str.replace(href, 'itemprop="url">', '')
		a_tag = str.replace(itemprop, '</a>', '')
		quotations = str.replace(a_tag, '"', '')
		url = str.replace(quotations, '<a href=', 'www.dailymail.co.uk')
		print(url)
		print("\n")

		#Sends article URL and title to email
		# msg = MIMEMultipart()
		# msg['From'] = 'ashleyc13@hotmail.co.uk'
		# msg['To'] = 'ashleyc13@hotmail.co.uk'
		# msg['Subject'] = keyword + ' article found!'
		# password = 'kuzuZUD3'
        #
		# body = url
		# msg.attach(MIMEText(body, 'html'))
		# print(msg)
        #
		# server = smtplib.SMTP("smtp-mail.outlook.com")
		# server.starttls()
		# server.login(msg['From'], password)
		# server.sendmail(msg['From'], msg['To'], msg.as_string())
		# server.quit()


for contain in small_containers:

	title_container = contain.findAll("h2", {"class":"linkro-darkred"})
	href = str(contain.a)

	#prints the URL and title if any results are found
	if keyword in href.lower():
		itemprop = str.replace(href, 'itemprop="url">', '')
		a_tag = str.replace(itemprop, '</a>', '')
		quotations = str.replace(a_tag, '"', '')
		url = str.replace(quotations, '<a href=', 'www.dailymail.co.uk')
		print(url)
		print("\n")

		#Sends article URL and title to email
#		msg = MIMEMultipart()
#		msg['From'] = 'ashleyc13@hotmail.co.uk'
		# msg['To'] = 'ashleyc13@hotmail.co.uk'
		# msg['Subject'] = keyword + ' article found!'
		# password = 'kuzuZUD3'
        #
		# body = url
		# msg.attach(MIMEText(body, 'html'))
		# print(msg)
        #
		# server = smtplib.SMTP("smtp-mail.outlook.com")
		# server.starttls()
		# server.login(msg['From'], password)
		# server.sendmail(msg['From'], msg['To'], msg.as_string())
		# server.quit()
