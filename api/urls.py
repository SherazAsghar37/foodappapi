from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from api.views import FoodViewset,ProductsViewset,Register,Signin,CurrentUserView
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'food',FoodViewset)
router.register(r'products',ProductsViewset)
urlpatterns = [
    path('',include(router.urls)),
    # path('',FoodViewset.as_view())
    path('auth/login/',obtain_auth_token,name="create-token"),
    path('auth/register/',Register.as_view()),
    path('auth/signin/',Signin.as_view()),
    path('auth/userdata/',CurrentUserView.as_view())
]

