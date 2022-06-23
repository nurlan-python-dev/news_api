from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from task.views import TaskListAPIView
from accounts.views import UserListAPIView
import private_storage.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_my/', include('task.urls')),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('api/v1/tasklist/', TaskListAPIView.as_view()),
    path('api/v1/userlist/', UserListAPIView.as_view()),
    path('p_media/', include(private_storage.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)