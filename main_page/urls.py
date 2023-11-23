from django.urls import path
from .views import MainView, FilmDetailView

urlpatterns = [
    path('', MainView.as_view()),
    path('film_detail/<int:id>/', FilmDetailView),
]