from django.urls import path, include
from rest_framework import routers
from . import views # Access views module in current directory

# Routers for API
router = routers.DefaultRouter()
router.register('api', views.BlogViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.get_post, name="get post"),
    path('comments/', views.get_comment_from_user, name='get comment'),
]

# Append these routes to the current urlpatterns
urlpatterns += [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]