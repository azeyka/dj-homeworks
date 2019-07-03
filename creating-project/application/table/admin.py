from django.contrib import admin

from table.models import Table, Path


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    pass