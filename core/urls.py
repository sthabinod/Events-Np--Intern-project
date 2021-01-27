from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'FAQ', views.FAQViewSet)
router.register(r'Contact', views.ContactViewSet)

urlpatterns = [
    path('',include(router.urls)),

]
