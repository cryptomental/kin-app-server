# tester config file. should be overwritten by ansible in prod/stage.

DEPLOYMENT_ENV = 'test'
DEBUG = True
DB_CONNSTR = "this gets overwritten by the tester code. it acutally uses a temp postgress db on the local disc"
REDIS_ENDPOINT = 'localhost'
REDIS_PORT = 6379

STELLAR_TIMEOUT_SEC = 10 # waitloop for tx data to be available
STELLAR_INITIAL_ACCOUNT_BALANCE = 10

ESHU_USERNAME = ''
ESHU_PASSWORD = ''
ESHU_HEARTBEAT = ''
ESHU_APPID = ''
ESHU_VIRTUAL_HOST = ''
ESHU_EXCHANGE = ''
ESHU_QUEUE = ''
ESHU_RABBIT_ADDRESS = ''
GCM_TTL_SECS = 60*60

STELLAR_BASE_SEED = ''
STELLAR_HORIZON_URL = 'https://horizon-kik.kininfrastructure.com/'
STELLAR_NETWORK = 'CUSTOM'
STELLAR_CHANNEL_SEEDS = ['']
STELLAR_KIN_ISSUER_ADDRESS = 'GBOJSMAO3YZ3CQYUJOUWWFV37IFLQVNVKHVRQDEJ4M3O364H5FEGGMBH'
STELLAR_PUBLIC_ADDRESS = 'GBYNGCLKPGC5YLABEHAPVB4YKGME7TKP6PZ3MSW56BBQM2MMIPBK4KSJ'

MAX_SIMULTANEOUS_ORDERS_PER_USER = 2
ORDER_EXPIRATION_SECS = 15
TASK_ALLOCATION_POLICY = 'default'

KMS_KEY_AWS_REGION = 'us-east-1'
STELLAR_BASE_SEED_CIPHER_TEXT_BLOB = 'something'
ENCRYPTED_STELLAR_BASE_SEED = 'some_other_thing'
STELLAR_CHANNEL_SEEDS_CIPHER_TEXT_BLOB = 'something'
ENCRYPTED_STELLAR_CHANNEL_SEEDS = ['some_other_thing']
