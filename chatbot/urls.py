from django.urls import path
from .views import get_game_data

urlpatterns = [
    path('game-data/', get_game_data, name='get_game_data'),
]
