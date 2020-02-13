from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, ScoreboardView


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('scores', ScoreboardView.as_view()),
    path('', include(router.urls))
]
