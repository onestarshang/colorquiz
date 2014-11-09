from django.contrib import admin                                                                                    
from colorquiz.models import LanguageColor
# Register your models here.

class LanguageColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'language_code', 'language_color', 'language_str')
admin.site.register(LanguageColor, LanguageColorAdmin)
