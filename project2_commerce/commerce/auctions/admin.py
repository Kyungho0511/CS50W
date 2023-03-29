from django.contrib import admin

from .models import Auctions, Bids, Comments


class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','starting_price', 'current_price', 'username', 'closed')


class BidsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'winner', 'bids', 'closed')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'auction_id', 'username', 'contents')


# Register your models here.
admin.site.register(Auctions, AuctionsAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Comments, CommentsAdmin)