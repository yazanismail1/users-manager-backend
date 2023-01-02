from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users_data.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
]
