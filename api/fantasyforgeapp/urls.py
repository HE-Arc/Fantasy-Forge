from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r"characters", views.CharacterViewSet, basename="characters")
router.register(r"auth", views.AuthViewSet, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
    #path("auth/register", views.RegisterView.as_view(). name="register")
]