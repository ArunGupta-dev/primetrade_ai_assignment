from django.urls import path
from trade_notes.views import*


urlpatterns = [
        path('create/', create_note),
        path('update/', update_note),
        path('delete/', delete_note),
        path('get/', TradeNoteViewSet.as_view({
            'get':'list'
            }), name='tradenotes')
]

