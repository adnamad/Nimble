from django.shortcuts import render
from .rss_extractor import extractor
from .models import Articles
from .forms import contactForm

def home(request):
    obj = extractor()
    title_news = obj['channel']['title']
    image_url = obj['channel']['image']['url']

    asp = Articles.objects.all()[::-1]
    for news in obj.entries:
        entry_img = news.media_thumbnail[0]["url"]
        entry_title = news.title
        entry_sum = news.summary
        for ob in asp:
            if entry_title == ob.title:
                break
        else:
            a = Articles(title=entry_title, summary=entry_sum, img_url=entry_img)
            a.save()
            asp = Articles.objects.all()[::-1]

    asp = Articles.objects.all()[::-1]
    context = {
        "ent": asp
    }
    return render(request,'home.html',context)

    if request.user.is_authenticated() and request.user.is_staff:
        # print(signup.objects.all())
        # i = 1
        # for instance in signup.objects.all():
        #   print(i)
        #   print(instance.Name)
        #   i += 1

        queryset = signup.objects.all().order_by('-timestamp')#.filter(Name__iexact="abc").count()

        context = {
            "queryset": queryset
        }

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
        to_email = [from_email,'your_other_email']
        contact_message = "%s: %s via %s"%(form_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, [to_email], fail_silently=False)


    context = {
        "template_title": title,
        "contact_form": form,
    }

    return render(request, "forms.html", context)
