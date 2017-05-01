from fraud_detection.settings import BASE_API_URL

from django.conf.urls import url

from graphs import views

urlpatterns = [
    url(r'^' + BASE_API_URL + 'graph/collision/$', views.NodeCollision.as_view()),
    url(r'^' + BASE_API_URL + 'graph/node/collision/$', views.NodeDetail.as_view()),
]
