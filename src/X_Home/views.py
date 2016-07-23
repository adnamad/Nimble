from django.shortcuts import render

# Create your views here.

from .rss_extractor import extractor
from .models import Articles

def home(request):

	title="Hello There !"	
	obj=extractor()
	title_news=obj['channel']['title']
	image_url=obj['channel']['image']['url']

	# for news in obj.entries:

	# 	entry_img=news.media_thumbnail[0]["url"]
	# 	entry_title=news.title
	# 	entry_sum=news.summary

	# 	a = Articles(title=entry_title,summary=entry_sum,img_url=entry_img)
	# 	a.save()

	asp=Articles.objects.all()[::-1][15:40]
	print(asp[0].title)	

	print(image_url)
	context={

			# "title_context":title,
			# "title_news":title_news,
			# "img_link":entry_img,
			# "entry_title":entry_title,
			# "entry_sum":entry_sum,
			"ent":asp

			}

	return render(request,"home.html",context)
