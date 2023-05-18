from django.contrib import admin
from .models import FootballClub , Player

# Register your models here.

# 1st Way to Register model in ADMIN Panel
admin.site.register(FootballClub)


# 2nd Way to Register model in ADMIN Panel
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name','country','price','desc']
