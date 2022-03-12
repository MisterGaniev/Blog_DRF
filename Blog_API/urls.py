from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_app.views import *

router = DefaultRouter()
router.register('maqola', MaqolaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image/', ImageCreateList.as_view()),
    path('image/<int:pk</', ImageDelete.as_view()),
    path('', include(router.urls)),
]
