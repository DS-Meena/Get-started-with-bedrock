import json
import boto3
import os

# Initialize the Bedrock runtime client
bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='ap-south-1')

def invoke_bedrock_model(prompt, model_id='amazon.titan-text-express-v1'):
    try:

        prompt = "Are aliens coming?"

        # Prepare the request body
        request_body = json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 300,
                "temperature": 0.5,
                "topP": 0.9,
                "stopSequences": ["User:"]
            }
        })

        # Invoke the model
        response = bedrock_runtime.invoke_model(
            body=request_body,
            modelId=model_id,
            accept='application/json',
            contentType='application/json'
        )

        # Parse and return the response
        response_body = json.loads(response.get('body').read())
        return response_body.get('results')
    
    except Exception as e:
        print(f"Error invoking Bedrock model: {e}")
        return None

# Example usage
prompt = "What is the capital of India?"
response = invoke_bedrock_model(prompt)

if response:
    print("Response from Bedrock model:")
    print(response)
else:
    print("Failed to get a response from the Bedrock model.")