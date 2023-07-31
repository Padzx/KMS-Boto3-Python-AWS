### Created a Key of KMS within Boto3 in Python 

# Importing the libs 

import boto3
import json
import logging
from datetime import date, datetime
import boto3
from botocore.exceptions import ClientError

# Setting the region

AWS_REGION = "us-east-2"
kms_client = boto3.client("kms", region_name = AWS_REGION)

# Logger Setting 

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format= '%(asctime)s: %(levelname)s: %(message)s')

# Creating the KMS in the default reagion 
kms_client = boto3.client('kms', region_name = AWS_REGION)

# Creating Function "json_datetime_serializer"
def json_datetime_serializer(obj):

    # Applying the condtional 
    if isinstance(obj, (datetime, date)):

        return obj.isoformat()
    
    raise TypeError("Type %s not serializable" % type(obj))

# Creating the function 'create_kms_key'
def create_kms_key():
    
    try:
        
        response = kms_client.create_key(Description = 'padzx-kms-python',
                                         Tags = [{
                                             
                                             'TagKey': 'Name',
                                             'TagValue': 'hands-on-cloud-cmk'
                                         }])
        
    except ClientError:

        logger.exception('Could Not Create a CMK Key.')
        raise

    else:

        return response 
    
# if condition 
if __name__  == '__main__':

    # Contants 

    logger.info('Creating a symetric CMK...')
    kms  = create_kms_key()
    logger.info(

        f'Symetric CMK is created within details: {json.dumps(kms, indent = 4, default = json_datetime_serializer)}'
        
        )
