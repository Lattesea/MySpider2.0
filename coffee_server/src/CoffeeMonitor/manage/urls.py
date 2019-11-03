
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('map', views.map_views)
    # path('download.html', views.download),
    # path('login.html', views.login),
    # path('<int:id>.html', views.model_index)
]
