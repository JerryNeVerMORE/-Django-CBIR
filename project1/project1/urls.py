"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ins import views as iv
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', iv.index1),
    url(r'^regist/$', iv.regist),
    url(r'^login/$',iv.login),
    url(r'^logout/$', iv.logout),
    url(r'^article/(?P<uploader>\w+)$', iv.article,name='article'),
    url(r'^(?P<id>\d+)/$',iv.detail, name='detail'),
    url(r'^index1/$',iv.index1),
    url(r'^upload/$', iv.upload , name='upload'),
    url(r'^latest/$',iv.latest),
    url(r'^result/(?P<id>\d+)$',iv.result,name='result')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
