from django.urls import path
from blog.api.views import GetBlogDetail , GetBLogListAndCreate

#makale_list_create_api_views , blog_detail

urlpatterns = [

    path("blog" , GetBLogListAndCreate.as_view() ,name="makale-list"),
    path("blog/<int:pk>" , GetBlogDetail.as_view() , name="blog-detail")


]
