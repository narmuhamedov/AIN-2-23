from django.urls import path
from .views import main_view, film_detail_view

urlpatterns = [
    path('main_page/', main_view),
    path('film_detail/<int:id>/', film_detail_view),
]