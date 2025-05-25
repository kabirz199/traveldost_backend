from django.contrib import admin
from .models import Group, Trip,InstagramModel

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'trip_count')   # Columns shown in list view
    search_fields = ('name', 'about_us')           # Search box fields
    list_filter = ('name',)                         # Filters on right sidebar
    readonly_fields = ('trip_count',)               # Make trip_count read-only if desired
    ordering = ('name',)                            # Default ordering

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_spot', 'group', 'destination', 'price', 'duration')
    search_fields = ('trip_spot', 'destination')
    list_filter = ('group', 'duration')
    ordering = ('trip_spot',)

@admin.register(InstagramModel)
class InstagramModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'url')   # Columns visible in list view
    search_fields = ('username', 'name')         # Search by username or name
    list_per_page = 20                            # Pagination, 20 per page
