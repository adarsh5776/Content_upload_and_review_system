from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import upload_csv, MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("upload-csv/", upload_csv, name="upload-csv"),
    path("", include(router.urls)),
]
