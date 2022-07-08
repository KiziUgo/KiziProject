from django.urls import path
from django.contrib import admin
from .views import (
    SearchCarView,
    PostListView,
    PostListCarView,
    PostListTechView,
    PostCreateCarView,
    PostCreateTechView,
    UserPostListCarView,
    UserPostListTechView,
    AddCommentCarView,
    AddCommentTechView,
    PostDetailTechView,
    PostDetailCarView,
    LikeCarView,
    LikeTechView,
    UnLikeCarView,
    UnLikeTechView,
    PostUpdateCarView,
    PostDeleteCarView,
    PostUpdateTechView,
    PostDeleteTechView,

)

app_name = 'MyBlogApp'

urlpatterns = [
    path('', PostListView.as_view(), name='MyBlogApp-welcome'),
    path('cars/', PostListCarView.as_view(), name='cars'),
    path('tech/', PostListTechView.as_view(), name='tech'),
    path('cars/carpost/<int:pk>/', PostDetailCarView.as_view(), name='carpost-postcars_detail'),
    path('tech/techpost/<int:pk>/', PostDetailTechView.as_view(), name='techpost-posttech_detail'),
    path('cars/usercars/<str:username>', UserPostListCarView.as_view(), name='usercars-postscars'),
    path('tech/usertech/<str:username>', UserPostListTechView.as_view(), name='usertech-poststech'),
    path('tech/techpost/new/', PostCreateTechView.as_view(), name='techpost-techcreate'),
    path('cars/carpost/new/', PostCreateCarView.as_view(), name='carpost-createcars'),
    path('cars/post/<int:pk>/update/', PostUpdateCarView.as_view(), name='carpost-updatecars'),
    path('cars/post/<int:pk>/delete/', PostDeleteCarView.as_view(), name='carpost-deletecars'),
    path('tech/post/<int:pk>/update/', PostUpdateTechView.as_view(), name='techpost-updatetech'),
    path('tech/post/<int:pk>/delete/', PostDeleteTechView.as_view(), name='techpost-deletetech'),
    path('cars/likecars/<int:pk>', LikeCarView, name='likecars_postcars'),
    path('tech/liketech/<int:pk>', LikeTechView, name='liketech_posttech'),
    path('cars/unlikecars/<int:pk>', UnLikeCarView, name='unlikecars_postcars'),
    path('tech/unliketech/<int:pk>', UnLikeTechView, name='unliketech_posttech'),
    path('cars/add_commentCars/<int:pk>/commentCars/', AddCommentCarView.as_view(), name='add_commentCars'),
    path('tech/add_commentTech/<int:pk>/commentTech/', AddCommentTechView.as_view(), name='add_commentTech'),
    path('searchcar/', SearchCarView.as_view(), name='searchcar'),
]