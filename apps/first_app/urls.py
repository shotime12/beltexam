from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.addPage),
    url(r'^logout$', views.logout),
    url(r'^addtrip$', views.addTrip),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^destination/(?P<id>\d+)$', views.destination)

]
