from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import RestaurantForm
from .models import Restaurant,ExcludedRestaurants
from datetime import date
import random

@login_required
def home(request):
    return render(request,'restaurant_picker/home.html',{})

@login_required
def add_restaurant(request):
    if request.method == "POST":
        restaurant_form = RestaurantForm(request.POST)
        if restaurant_form.is_valid():
            new_item = restaurant_form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect("/restaurant_picker")
    else:
        restaurant_form = RestaurantForm()

    return render(request,'restaurant_picker/add.html',{'restaurant_form': restaurant_form})

@login_required
def pick_restaurant(request):
    restaurants_to_exclude = ExcludedRestaurants.objects.all().filter(user=request.user)
    current_week = date.today().isocalendar()[1]
    restaurants_to_exclude = restaurants_to_exclude.filter(date__week=current_week)
    restaurants_to_exclude = [object.restaurant.name for object in restaurants_to_exclude]
    restaurants_to_pick = Restaurant.objects.exclude(name__in=restaurants_to_exclude)
    if not restaurants_to_pick:
        ExcludedRestaurants.objects.all().filter(user=request.user).delete()
        restaurants_to_pick = Restaurant.objects.all()
        result = random.choice(restaurants_to_pick)
        ExcludedRestaurants.objects.create(user=request.user,restaurant=result)
    else:
        result = random.choice(restaurants_to_pick)
        ExcludedRestaurants.objects.create(user=request.user,restaurant=result)

    return render(request,'restaurant_picker/pick.html',{'result': result})