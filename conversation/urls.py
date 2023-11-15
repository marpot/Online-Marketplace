from django.urls import path 

from . import views
from .views import new_conversation

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('detail/<int:pk>', views.detail, name='detail'),
]
