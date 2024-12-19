"""this module contains all url of the app"""

from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Contact
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create', views.create, name='create'),
    path('contact/<int:contact_id>/upadate/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
]
