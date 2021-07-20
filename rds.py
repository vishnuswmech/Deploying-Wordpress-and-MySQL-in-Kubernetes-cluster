import boto3
import config
import numpy as np
import pandas as pd
rds = boto3.client("rds",
                  region_name='us-east-1',
                  aws_access_key_id= config.access_key,
                  aws_secret_access_key= config.secret_key)


response = rds.describe_db_instances( )


print(type(response))
