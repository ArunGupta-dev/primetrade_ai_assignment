from django.contrib import admin
from .models import trade_notes

@admin.register(trade_notes)
class TradeNoteAdmin(admin.ModelAdmin):
    list_display = ('market_symbol', 'author', 'created_on', 'updated_on')
    list_filter = ('created_on', 'author')
    search_fields = ('market_symbol', 'trading_thesis')
    readonly_fields = ('note_id', 'created_on', 'updated_on')
