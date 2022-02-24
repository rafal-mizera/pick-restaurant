from django.urls import path
from . import views

app_name = 'restaurant_picker'

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_restaurant,name='add'),
    path('pick/',views.pick_restaurant,name='pick'),
    ]