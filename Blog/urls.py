from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about")
]

urlpatterns += staticfiles_urlpatterns()
