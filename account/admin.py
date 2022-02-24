from django.contrib import admin

# Register your models here.
@admin.register
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'phone_number','notes']