# -*- coding: utf-8 -*-
"""
This is for AWS Stepfunctions E2E Test.
"""
from error import ErrorOrderCreate, AlreadyRunning


def test_state_machine(order_event):
    if 'OP1-' in order_event['order_id']:
        raise ErrorOrderCreate('testing scenario')
    if 'OP2-' in order_event['order_id']:
        raise AlreadyRunning('testing scenario')
    if 'OP3-' in order_event['order_id']:
        raise Exception('testing scenario')
