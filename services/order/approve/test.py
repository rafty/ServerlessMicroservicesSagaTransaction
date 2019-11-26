# -*- coding: utf-8 -*-
"""
This is for AWS Stepfunctions E2E Test.
"""
from error import ErrorOrderUpdate


def test_state_machine(order_event):
    if 'OA1-' in order_event['order_id']:
        raise ErrorOrderUpdate('testing scenario')
    if 'OA2-' in order_event['order_id']:
        raise Exception('testing scenario')


