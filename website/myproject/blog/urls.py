from django.urls import path
from . import views # Access views module in current directory

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.get_post, name="get post"),
    path('comments', views.get_comment_from_user, name='get comment'),
]
