import os

HOME_DIR = os.path.dirname( __file__ )

BIN_DIRNAME = 'python-jq-bin'

EXEC_NAME = 'jq'

OUTPUT_DIR = os.path.abspath(os.path.join(HOME_DIR, BIN_DIRNAME))

JQ_PATH = os.path.abspath(os.path.join(HOME_DIR, BIN_DIRNAME, EXEC_NAME))