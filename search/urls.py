from django.urls import path, include

from search import views

app_name = 'search'
urlpatterns = [
    path('', views.ESearchView.as_view(), name='index'),
]
