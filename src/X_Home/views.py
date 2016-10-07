from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .newsapi import news_miner ,get_description
from .models import Articles
from .forms import contactForm
from .newsclf import clf

def home(request):
    # obj = news_miner()
    # asp = Articles.objects.all()[::-1]
    # for news in obj:
    #     # timest = news['webPublicationDate']
    #     entry_title = news['webTitle']
    #     entry_category = clf(entry_title)
    #     entry_link = news['webUrl']
    #     entry_sum = get_description(entry_link)
    #     entry_img =   news['fields']['thumbnail']

    #     for ob in asp:
    #         if entry_title == ob.title:
    #             break
    #     else:
    #         a = Articles(title=entry_title, img_url=entry_img, page_link = entry_link,summary = entry_sum, category = entry_category)
    #         a.save()
    #         asp = Articles.objects.all()[::-1]

    
    asp = Articles.objects.all()[::-1]
    w_obj = []
    p_obj = []
    s_obj = []
    t_obj = []
    f_obj = []
    c_obj = []
    b_obj = []
    for X in asp:
        if X.category == 'world':
            w_obj.append(X)
        elif X.category == 'politics':
            p_obj.append(X)
        elif X.category == 'tech':
            t_obj.append(X)
        elif X.category == 'football':
            f_obj.append(X)
        elif X.category == 'sports':
            s_obj.append(X)
        elif X.category == 'culture':
            c_obj.append(X)
        else:
            b_obj.append(X)



    context = {
        "ent": asp,
        "wobj": w_obj[:14],
        "sobj": s_obj[:7],
        "fobj": f_obj[:10],
        "cobj": c_obj[:7],
        "bobj": b_obj[:10],
        "pobj": p_obj[:10],
        "tobj": t_obj[:10],
    }
    return render(request,'home.html',context)


def world(request):
    asp = Articles.objects.all()[::-1]
    w_obj = []

    for X in asp:
        if X.category == 'world':
            w_obj.append(X)

    context = {
         "abc": w_obj,
    } 

    return render(request,'world.html', context)

def politics(request):
    asp = Articles.objects.all()[::-1]
    p_obj = []

    for X in asp:
        if X.category == 'politics':
            p_obj.append(X)

    context = {
         "abc": p_obj,
    } 

    return render(request,'politics.html', context)

def buisness(request):
    asp = Articles.objects.all()[::-1]
    b_obj = []

    for X in asp:
        if X.category == 'business':
            b_obj.append(X)

    context = {
         "abc": b_obj,
    } 

    return render(request,'buisness.html', context)

def tech(request):
    asp = Articles.objects.all()[::-1]
    t_obj = []

    for X in asp:
        if X.category == 'tech':
            t_obj.append(X)

    context = {
         "abc": t_obj,
    } 

    return render(request,'tech.html', context)

def football(request):
    asp = Articles.objects.all()[::-1]
    f_obj = []

    for X in asp:
        if X.category == 'football':
            f_obj.append(X)

    context = {
         "abc": f_obj,
    } 

    return render(request,'football.html', context)

def sports(request):
    asp = Articles.objects.all()[::-1]
    s_obj = []

    for X in asp:
        if X.category == 'sports':
            s_obj.append(X)

    context = {
         "abc": s_obj,
    } 

    return render(request,'sports.html', context)

def culture(request):
    asp = Articles.objects.all()[::-1]
    c_obj = []

    for X in asp:
        if X.category == 'culture':
            c_obj.append(X)

    context = {
         "abc": c_obj,
    } 

    return render(request,'culture.html', context)


def contact(request):
    title = "Enter your Details"
    form = contactForm(request.POST or None)
    if form.is_valid():
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
