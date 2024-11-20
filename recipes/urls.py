from django.urls import path

from recipes.views import home, contato, sobre


#HTTP REQUEST <- HTTP RESPONSE


urlpatterns = [
    path('',home), #Home
    path('contato/', contato),
    path('sobre/', sobre),
]