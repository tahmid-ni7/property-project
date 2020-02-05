from django.contrib import admin
from realtors.models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name','phone')
admin.site.register(Realtor,RealtorAdmin)
