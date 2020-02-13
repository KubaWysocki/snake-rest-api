from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from rest_framework_simplejwt import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include('api.urls')),
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
