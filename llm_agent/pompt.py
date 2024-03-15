import boto3
import json

brt = boto3.client(service_name='bedrock-runtime')

# json body depends on the model
body = json.dumps({
    "inputText": "do you know abouut IPL",
    "textGenerationConfig": {
        "maxTokenCount": 300,
        "stopSequences": [],
        "temperature": 0.1,
        "topP": 0.9,
    },
})

modelId = 'amazon.titan-text-lite-v1'
accept = 'application/json'
contentType = 'application/json'

"""
    Using Boto3 you need to replicate the correct API call.
"""
response = brt.invoke_model(body=body, modelId=modelId, contentType=contentType)

# response type can be different for different models
response_body = json.loads(response.get('body').read())

# text
print(response_body['results'][0])