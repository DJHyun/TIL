from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/delete', views.movie_delete, name='movie_delete'),
    path('<int:movie_id>/scores/new', views.create_score, name='create_score'),
    path('<int:movie_id>/scores/<int:score_id>/delete', views.delete_score, name='delete_score'),
]
