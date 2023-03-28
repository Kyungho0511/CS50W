from django.contrib import admin

from .models import Auctions, Bids


class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','starting_price', 'current_price', 'username', 'closed')


class BidsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'winner', 'bids', 'closed')


# Register your models here.
admin.site.register(Auctions, AuctionsAdmin)
admin.site.register(Bids, BidsAdmin)