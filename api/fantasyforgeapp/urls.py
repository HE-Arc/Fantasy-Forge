from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r"characters", views.CharacterViewSet, basename="characters")

urlpatterns = [
    path("", include(router.urls)),
    #path("api/characters/", UserCharactersView.as_view(), name="user-characters"),
]