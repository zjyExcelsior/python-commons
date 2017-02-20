# coding: utf-8
from raven import Client
from logger import get_logger

raven_logger = get_logger('raven')

DSN = 'https://<key>:<secret>@app.getsentry.com/<project>'

client = Client(dsn=DSN)
# 用于将raven端的异常记录下来
client.error_logger = raven_logger
client.uncaught_logger = raven_logger

client.captureMessage('test...')
try:
    100/0
except ZeroDivisionError:
    client.captureException()