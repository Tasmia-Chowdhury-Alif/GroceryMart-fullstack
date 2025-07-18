from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register("categories", views.CategoryViewSet)
router.register("brands", views.BrandViewSet)
router.register("products", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

