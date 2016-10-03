from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

from .newsapi import news_miner #,get_description
from .models import Articles
from .forms import contactForm
from .newsclf import clf
import requests
from bs4 import BeautifulSoup


def home(request):
    obj = news_miner()
    asp = Articles.objects.all()[::-1]
    for news in obj[:10]:
        # timest = news['webPublicationDate']
        entry_title = news['webTitle']
        entry_category = clf(entry_title)
        # print(entry_category)
        entry_link = news['webUrl']
        # entry_sum = get_description(entry_link)
        # if entry_sum:
        # print(entry_sum.encode('utf8'))
        entry_img =   news['fields']['thumbnail']                
        


        # entry_prediction = clf(entry_title)
        for ob in asp:
            if entry_title == ob.title:
                break
        else:
            a = Articles(title=entry_title, img_url=entry_img, page_link = entry_link, category = entry_category)
            
            a.save()
            asp = Articles.objects.all()[::-1]

    
    # print(asp[2].title)
    # print(asp[2].summary)
    asp = Articles.objects.all()[::-1]
    context = {
        "ent": asp
    }
    # return render(request,'culture.html',context)
    return render(request,'home1.html',context)


    # if request.user.is_authenticated() and request.user.is_staff:
    #     # print(signup.objects.all())
    #     # i = 1
    #     # for instance in signup.objects.all():
    #     #   print(i)
    #     #   print(instance.Name)
    #     #   i += 1

    #     queryset = signup.objects.all().order_by('-timestamp')#.filter(Name__iexact="abc").count()

    #     context = {
    #         "queryset": queryset
    #     }

def contact(request):
    title = "Enter your Details"
    form = contactForm(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data)
        form_email = form.cleaned_data.get("Email")
        form_message = form.cleaned_data.get("Message")
        form_name = form.cleaned_data.get("Name")

        subject = 'site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = "%s: %s via %s"%(form_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, [to_email], fail_silently=False)


    context = {
        "template_title": title,
        "contact_form": form,
    }

    return render(request, "forms.html", context)
