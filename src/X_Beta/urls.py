from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from X_Home.views import home,contact,world,sports,football,tech,culture,buisness,politics
from registration.backends.default import urls as urls1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',home,name='home'),
	url(r'^world/',world, name ='world'),
	url(r'^culture/',culture, name ='culture'),
	url(r'^politics/',politics, name ='politics'),
	url(r'^buisness/',buisness, name ='buisness'),
	url(r'^football/',football, name ='football'),
	url(r'^sports/',sports, name ='sports'),
	url(r'^tech/',tech, name ='tech'),
    url(r'^contact/',contact, name ='contact'),
    url(r'^accounts/', include(urls1)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)