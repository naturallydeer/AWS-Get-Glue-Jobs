import boto3

client = boto3.client('glue', region_name='eu-west-1')

# paginate to get list of all jobs
paginator = client.get_paginator(operation_name='get_jobs')

# create empty lists
df1=[] 
df2=[] 

for page in paginator.paginate():
  jobs = page['Jobs']
 

for key in jobs:
   try:
     df1.append(key['Name']) 
     df2.append(key['GlueVersion']) 
   except KeyError:
     df2.append(0)
      
res = list(zip(df1,df2)) 
 
for row in res: 
    print(''.join(f'{x:^8}' for x in row)) # 8-character wide centered columns 
