# -*- coding: utf-8 -*-
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute
)


# --------------------------
# Order Table
# --------------------------
class Order(Model):
    class Meta:
        table_name = 'Order'
        region = 'ap-northeast-1'
        max_retry_attempts = 8
        base_backoff_ms = 297

    order_id = UnicodeAttribute(hash_key=True)
    order_status = UnicodeAttribute()
    cause = UnicodeAttribute(null=True)
