from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import generate_random_stats

router = DefaultRouter()
router.register(r"characters", views.CharacterViewSet, basename="characters")
router.register(r"auth", views.AuthViewSet, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
    path("generate-stats/", generate_random_stats, name="generate-stats"),
]