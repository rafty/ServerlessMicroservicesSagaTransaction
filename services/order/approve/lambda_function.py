# -*- coding: utf-8 -*-
import logging
import json
import datetime
from aws_xray_sdk.core import patch_all
from pynamodb.exceptions import UpdateError
from model import Order
from error import ErrorOrderApprove

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()


def util_pynamodb_model_json_serialize(model):
    class ModelEncoder(json.JSONEncoder):
        def default(self, obj):
            if hasattr(obj, 'attribute_values'):
                return obj.attribute_values
            elif isinstance(obj, datetime.datetime):
                return obj.isoformat()
            return json.JSONEncoder.default(self, obj)

    model_json = json.dumps(model, cls=ModelEncoder)

    return model_json


def extract_order(event):
    return event


def approve_order(_order):
    # orderはstatusだけ変更するのでupdate()
    # payment,inventoryはtransactionも変更するので上書きsave()

    status = 'Approved'
    logger.info('update: {}, status:{}'.format(_order, status))

    try:
        order = Order(_order['order_id'])
        order.update(
            actions=[
                Order.order_status.set(status)
            ]
        )
        return order

    except UpdateError as e:
        error_message = 'update_order Error: {}'.format(e)
        logging.exception(error_message)
        raise ErrorOrderUpdateStatus(error_message)


def pynamo_dict_serialize(order):
    order_json = util_pynamodb_model_json_serialize(order)
    order_dict = json.loads(order_json)
    return order_dict


def lambda_handler(event, context):

    logger.info('OrderApprove() event: {}'.format(event))
    order_event = extract_order(event)

    try:
        order = approve_order(order_event)

        ここから

        test_state_machine(order_event)

        order = pynamo_dict_serialize(order)
        return order

    except ErrorOrderApprove as e:
        raise e
    except Exception as e:
        logger.error(e)
        raise ErrorOrderApprove
