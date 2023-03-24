from django.contrib import admin

from .models import Auctions


class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'username')

# Register your models here.
admin.site.register(Auctions, AuctionsAdmin)