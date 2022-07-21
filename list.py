import boto3

# indicate AWS region in the second parenthesis
glue_client = boto3.client('glue', 'eu-west-1')

# paginate to get list of all jobs
paginator = glue_client.get_paginator(operation_name="get_jobs")
response_iterator = paginator.paginate()

# create empty lists
df1=[] 
df2=[] 

for page in response_iterator:
  jobs = page['Jobs']
 
  # specify variables of interest here
  for key in jobs:  
      df1.append(key['Name']) 
      df2.append(key['GlueVersion']) 

res = list(zip(df1,df2)) 
 
for row in res: 
    print(''.join(f'{x:^8}' for x in row)) # 8-character wide centered columns 
