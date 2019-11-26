# -*- coding: utf-8 -*-
"""
This is for AWS Stepfunctions E2E Test.
"""
from error import ErrorOrderReject


def test_state_machine(order_event):
    if 'OF1-' in order_event['order_id']:
        raise ErrorOrderReject('testing scenario')
    if 'OF2-' in order_event['order_id']:
        raise Exception('testing scenario')
