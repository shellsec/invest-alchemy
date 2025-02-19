from datetime import datetime
import os

AWS_REGION = 'us-east-1'
S3_BUCKET_NAME = 'i365.tech'
S3_DOUBLE_MA_BASE_DIR = 'invest-alchemy/data/strategy/double-ma/'
S3_PORTFOLIO_BASE_DIR = 'invest-alchemy/data/portfolio/'
LOCAL_BASE_DIR = '/tmp/invest-alchemy/'
OUTPUT_FILE = datetime.today().strftime('%Y%m%d') + '.txt'
SNS_TOPIC = 'arn:aws:sns:us-east-1:745121664662:trade-signal-topic'
TRADE_DATE_FORMAT_STR = '%Y%m%d'
TODAY_STR = datetime.today().strftime(TRADE_DATE_FORMAT_STR)
TG_CHATS = os.environ['TG_CHAT_IDS'].split(' ')
TG_SEND_MESSAGE_API='https://api.telegram.org/bot' + os.environ['TG_BOT_API_TOKEN'] + '/sendMessage'
STRATEGY_DMA_SHORT_TERM = 11
STRATEGY_DMA_LONG_TERM = 22
MAX_STRATEGY_SIGNAL_ERROR_COUNT = 5
RISK_FREE_INVEST_DEPOSIT_RATE = 0.0275 / 365 # Five-year fixed deposit rate in China(20220828)
PG_DB_NAME = 'postgres'
PG_PORT = 5432
PG_DB_URL = os.environ['PG_DB_URL']
PG_DB_USER = 'postgres'
PG_DB_PWD = os.environ['PG_DB_PWD']