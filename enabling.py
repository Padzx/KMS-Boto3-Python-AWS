# Importing the libs 

import boto3
import json
import logging
from datetime import date, datetime
import boto3
from botocore.exceptions import ClientError

# Enabling the Key 

AWS_REGION = 'us-east-2'

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format= '%(asctime)s: %(levelname)s: %(message)s')

# Creating the KMS in the default reagion 
kms_client = boto3.client('kms', region_name = AWS_REGION)


# Creating the function "enable_kms_key"

def enable_kms_key(key_id):
    
    try:
        
        response = kms_client.enable_key(KeyId = key_id)
        
    except ClientError:
        
        logger.exception('Could not enable a KMS Key.')
        raise
    
    else:
        return response 



if __name__ == '__main__':

    # Constants 

    KEY_ID = "1b0be2d3-c409-4423-b5d2-cc4007cab194"
    logger.info('Enabling a KMS Key...')
    kms = enable_kms_key(KEY_ID)
    logger.info(f'KMS key ID {KEY_ID} enable for use.')
