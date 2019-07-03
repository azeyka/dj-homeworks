from django.contrib import admin

from .models import Route, Station


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    search_fields = ['name']