from django.contrib import admin
from listings.models import Listing, AboutText


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'realtor', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','city')
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'price', 'city', 'zipcode', 'bedrooms')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)


class AboutTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_title', 'sub_title', 'is_published')
    list_display_links = ('id', 'about_title')
    list_editable = ('is_published',)


admin.site.register(AboutText, AboutTextAdmin)
