# -*- coding: utf-8 -*-
"""
Errors for StateMachine Catch.
"""


class ErrorPaymentDebit(Exception):
    pass


class DebitLimitExceeded(Exception):
    pass
