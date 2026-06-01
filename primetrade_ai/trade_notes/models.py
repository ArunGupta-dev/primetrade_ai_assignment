from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.


User = get_user_model()


class trade_notes(models.Model):
    note_id = models.UUIDField(
            primary_key = True,
            default = uuid.uuid4,
            editable = False
            )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    market_symbol = models.CharField(max_length = 50, default = 'NIL')
    trading_thesis = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
