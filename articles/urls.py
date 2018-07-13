from django.conf.urls import url
fron . import views

urlpatterns = [
    url(r'^$', views.index)
]
