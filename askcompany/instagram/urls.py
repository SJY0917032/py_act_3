from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL을 만들어준다. (패턴)
# router.urls # url pattern list

urlpatterns = [
    path('', include(router.urls)),
    path('public/', views.public_post_list),
]
