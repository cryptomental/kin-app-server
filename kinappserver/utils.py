from datadog import statsd
from flask import jsonify, config
from kinappserver import amqp_publisher, config

from kinappserver import config

ERROR_ORDERS_COOLDOWN = -1
ERROR_NO_GOODS = -2

KINIT_MEMO_PREFIX = '1-kit-'
ORDER_ID_LENGTH = 22


def increment_metric(metric_name, count=1):
    '''increment a counter with the given name and value'''
    # set env to undefined for local tests (which do not emit stats, as there's no agent)
    statsd.increment('kinitapp.%s.%s' % (config.DEPLOYMENT_ENV, metric_name), count)


def errors_to_string(errorcode):
    '''translate error codes to human-readable reasons'''
    if errorcode == ERROR_ORDERS_COOLDOWN:
        return 'orders-cooldown'
    elif errorcode == ERROR_NO_GOODS:
        return 'no-goods'
    else:
        print('should never happen')
        return 'unknown-error'

def seconds_to_utc_midnight():
    '''returs the (integer) number of seconds to the next midnight at utc'''
    from datetime import datetime, timedelta, timezone

    tomorrow = datetime.date(datetime.today() + timedelta(days=1))
    # convert date objevt to datetime. hack from https://stackoverflow.com/a/27760382/1277048
    tomorrow_dt = datetime.strptime(tomorrow.strftime('%Y%m%d'), '%Y%m%d')
    # calc hours until tomorrow
    return(int((tomorrow_dt - datetime.utcnow()).total_seconds()))


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class InternalError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def send_gcm(token, payload):
    payload_dict = {}
    payload_dict['message'] = payload
    amqp_publisher.send_gcm("eshu-key", payload_dict, [token], False, config.GCM_TTL_SECS)


def send_apns(token, payload):
    #TODO 
    pass