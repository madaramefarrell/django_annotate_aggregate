from django.contrib import admin
from .models import User, Brand, Moto


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand_name', 'price')

    def brand_name(self, obj):
        return obj.brand.name

admin.site.register(User, UserAdmin)
admin.site.register(Moto, MotoAdmin)
admin.site.register(Brand)
