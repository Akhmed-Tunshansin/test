
from django.urls import path,include
from rest_framework import routers
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('order', views.OrderViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('register_user/', views.user_register)

]