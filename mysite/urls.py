from django.contrib import admin
from django.urls import path, include  # ← This line should make `include` available.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]