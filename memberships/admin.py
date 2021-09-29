from django.contrib import admin
from .models import Memberships, Category


class MembershipsAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price_yearly',
        'price_monthly',
        'price_quarterly',
        'rating',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Memberships, MembershipsAdmin)
