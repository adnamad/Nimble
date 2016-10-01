from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from X_Home.views import home,contact
from registration.backends.default import urls as urls1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',home,name='home'),
    url(r'^contact/',contact, name ='contact'),
    url(r'^accounts/', include(urls1)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)