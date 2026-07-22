from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at')
    search_fields = ('title',)
    list_filter = ('category', 'price', 'created_at',)
    readonly_fields = ('created_at',) # apareça na tela de detalhes/edição, sem permitir alteração manual.

admin.site.register(models.Product, ProductAdmin)