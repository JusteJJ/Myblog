from django.urls import path
from .views import HomeView, ArticlesDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('articles/<int:pk>', ArticlesDetailView.as_view(), name='articles'),
    path('addarticle/', AddPostView.as_view(), name='add_post'),
    path('addcategory/', AddCategoryView.as_view(), name='add_category'),
    path('articles/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('articles/edit/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),

]
