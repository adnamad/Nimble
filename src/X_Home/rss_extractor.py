import feedparser
import webbrowser

def extractor() :
	d = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
	news_feed_title=d['channel']['title']
	news_feed_image=d['channel']['image']['url']
	print(d.feed.title)
	 # print(d)
	return d



