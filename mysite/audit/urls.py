from django.urls import path

from . import views

app_name = 'audit'
urlpatterns = [
    # ex: /audit/
    path('', views.index, name='audit-index'),
    # ex: /audit/contacts/
    path('contacts/', views.contact_list, name='contacts'),
    # ex: /audit/contacts/1/
    path('contacts/<int:person_id>/', views.contact_details),
    path('organization/', views.organization_list, name='Organization List'),
    path('organization/<int:organization_id>/', views.organization_details)
]
