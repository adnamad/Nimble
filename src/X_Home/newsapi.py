import requests, re
import pprint,csv
import json,urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

def news_miner():

	for page in range(1):
		url = "http://content.guardianapis.com/search?page-size=200&page=1&show-fields=thumbnail&section=sport%7Cfootball%7Cpolitics%7Cworld%7Cculture%7Ctechnology%7Cbusiness&order-by=newest&api-key=bf21288d-a1d8-4a30-96a4-ac0f0ccee597"
		response = requests.get(url)
		news = json.loads(response.text)
		return(news['response']['results'])






def get_description(final_url):
	cleaner =re.compile('<.*?>')
	source = requests.get(final_url)
	text = source.text
	raw_data = BeautifulSoup(text,'lxml')


	for items in raw_data.findAll('div',{'class': 'content__standfirst'}):
		items = str(items)
		cleantext = re.search(r'<m.*?>', items , re.M|re.I)
		if cleantext:
			clean = re.search(r'".*?"', cleantext.group() , re.M|re.I)
			return(clean.group())
		else:
			data = "Nothing here..!!"
			return(data)
