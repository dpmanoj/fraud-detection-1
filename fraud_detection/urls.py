from django.conf.urls import url, include
from django.contrib import admin
from graphs import views

urlpatterns = [
    url(r'^api/v1/docs/$', views.index, name='index'),
    url(r'^data/$', views.api_docs, name='docs'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('graphs.urls'))
]
