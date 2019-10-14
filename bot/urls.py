from django.urls import path

from bot.views import callback

urlpatterns = [
    path('callback', callback),
]