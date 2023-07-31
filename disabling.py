# Importing the libs 

import boto3
import json
import logging
from datetime import date, datetime
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-2'
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
kms_client = boto3.client("kms", region_name=AWS_REGION)

def disable_kms_key(key_id):
    """
    Sets the key state of a KMS key to disabled..
    """
    try:
        response = kms_client.disable_key(KeyId=key_id)
    except ClientError:
        logger.exception('Could not disable a KMS key.')
        raise
    else:
        return response

if __name__ == '__main__':
    # Constants
    KEY_ID = '1b0be2d3-c409-4423-b5d2-cc4007cab194'
    logger.info('Disabling a KMS key...')
    kms = disable_kms_key(KEY_ID)
    logger.info(f'KMS key ID {KEY_ID} disabled for use.')