from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('page/contact/', views.ContactDetailView.as_view(), name='contact'),
    path('page/fag/', views.FagDetailView.as_view(), name='fag'),

    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),

    path('category/<slug:category_slug>/', views.PostListView.as_view(), name='category'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
