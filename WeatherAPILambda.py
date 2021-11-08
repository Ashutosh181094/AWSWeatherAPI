import requests
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    city_name="Orlando"
    api_key="YOUR_API_KEY"
    
    url="http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key+"&units=metric"
    print("URL for API: ",url)
    result=requests.get(url)
    data_extracted=result.json()
    temp_orlando=data_extracted['main']['temp']
    subject = 'Temperature Information of Orlando'
    client = boto3.client("ses")
    body = """
                 <br>
                 This mail comes from AWS Lambda Event Scheduling.
                 Current temperature of Orlando is {}
                 .
         """.format(temp_orlando)
         
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "ashutoshrai181094@gmail.com", Destination = {"ToAddresses": ["ashutoshrai181094@gmail.com"]}, Message = message) 
    print("The mail is sent successfully")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
