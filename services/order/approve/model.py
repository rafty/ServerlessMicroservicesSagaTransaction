# -*- coding: utf-8 -*-
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    JSONAttribute,
    UTCDateTimeAttribute,
    BooleanAttribute,
    ListAttribute,
    MapAttribute
)
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection


"""
Order Table
"""
class Order(Model):
    class Meta:
        table_name = 'myOrder'
        region = 'ap-northeast-1'
        max_retry_attempts = 8
        base_backoff_ms = 297

    order_id = UnicodeAttribute(hash_key=True)
    order_status = UnicodeAttribute()
