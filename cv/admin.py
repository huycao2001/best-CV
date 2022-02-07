from django.contrib import admin
from .models import CV

class CVAdmin(admin.ModelAdmin):
    
    list_display=('title','description','is_published')
    search_fields =('title','description','is_published')
    list_per_page=25

admin.site.register(CV,CVAdmin)
