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
        "wobj": w_obj,
        "sobj": s_obj,
        "fobj": f_obj,
        "cobj": c_obj,
        "bobj": b_obj,
        "pobj": p_obj,
        "tobj": t_obj,
    }
    return render(request,'home1.html',context)

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
