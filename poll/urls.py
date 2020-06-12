from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    # path('monitor/',
    #      views.index, name='individual_monitor'),
    path('startpolling/',
         views.startpolling, name='start_polling'),
    path('monitor/<str:monitor_id>',
         views.individual_monitor, name='individual_monitor'),
]
