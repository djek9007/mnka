from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('category/contact/', views.ContactDetailView.as_view(), name='contact'),
    path('category/fag/', views.FagDetailView.as_view(), name='fag'),


    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),

    path('category/<slug:category_slug>/', views.PostListView.as_view(), name='category'),


    path('', views.PostListView.as_view(), name='home'),
]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
