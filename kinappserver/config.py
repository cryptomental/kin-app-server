# tester config file. should be overwritten by ansible in prod/stage.

DEBUG = True
DB_CONNSTR = "this gets overwritten by the tester code. it acutally uses a temp postgress db on the local disc"
REDIS_ENDPOINT = 'sth'
REDIS_PORT = 6379