from django.contrib import admin
from .models import Group, Trip,InstagramModel,TripImage

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'trip_count')   # Columns shown in list view
    search_fields = ('name', 'about_us')           # Search box fields
    list_filter = ('name',)                         # Filters on right sidebar
    readonly_fields = ('trip_count',)               # Make trip_count read-only if desired
    ordering = ('name',)                            # Default ordering


class TripImageInline(admin.TabularInline):  # or admin.StackedInline for a vertical layout
    model = TripImage
    extra = 1

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_spot', 'group', 'destination', 'price', 'duration','trip_priority', 'destination_priority')
    search_fields = ('trip_spot', 'destination')
    list_filter = ('group', 'duration')
    ordering = ('trip_spot',)
    inlines = [TripImageInline]
    list_editable = ['trip_priority', 'destination_priority']

@admin.register(InstagramModel)
class InstagramModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'url')   # Columns visible in list view
    search_fields = ('username', 'name')         # Search by username or name
    list_per_page = 20                            # Pagination, 20 per page


@admin.register(TripImage)
class TripImageAdmin(admin.ModelAdmin):
    list_display = ('trip', 'image')
