from django.urls import path
from .views import *


urlpatterns = [
    path('house/create/', HouseCreationView.as_view()),
    path('house/list/', HouseListView.as_view()),
    path('house/update/<int:pk>', HouseUpdateView.as_view()),

]