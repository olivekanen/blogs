from .views import post_list, post_detail
from django.urls import path, include

urlpatterns = [
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("", post_list, name="home"),
    #path("", include("blog.urls")),
]