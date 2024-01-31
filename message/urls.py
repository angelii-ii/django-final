from django.urls import path

from . import views

app_name='message'

urlpatterns=[
    path('inbox/',views.inbox, name='inbox'),
    path('<int:pk>/',views.detail,name='pm'),
    path('new/<int:item_pk>/',views.new_message,name='new')
]