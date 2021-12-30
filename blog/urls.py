from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import HomeView, PostDetailsView, PostList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts', PostList.as_view(), name='posts'),
    path('posts/<slug:slug>', PostDetailsView.as_view(), name='post_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
