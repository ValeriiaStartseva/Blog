from django.contrib import admin
from django.urls import path
from django.conf import settings
from posts.views import homepage, post, about, search, postlist, allposts
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('post/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('postlist/<slug>/', postlist, name='postlist'),
    path('posts/', allposts, name='allposts'),
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
