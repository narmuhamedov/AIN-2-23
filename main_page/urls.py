from django.urls import path
from .views import MainView, FilmDetailView, Search

urlpatterns = [
    path('', MainView.as_view()),
    path('film_detail/<int:id>/', FilmDetailView.as_view()),
    path("search/", Search.as_view(), name="search"),
]