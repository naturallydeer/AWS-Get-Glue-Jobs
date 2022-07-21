import boto3

glue_client = boto3.client('glue', 'eu-west-1')

paginator = glue_client.get_paginator(operation_name="get_jobs")
response_iterator = paginator.paginate()

for page in response_iterator:
  print(page) # return full json syntax with all variables
