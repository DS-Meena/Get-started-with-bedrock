import json
import boto3
import os

# Initialize the Bedrock runtime client
client = boto3.client(service_name='bedrock-runtime', region_name='ap-south-1')
model_id = "amazon.titan-text-express-v1"

def invoke_chat_bot(conversation, model_id='amazon.titan-text-express-v1'):
    try:
        # Invoke the model
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={
                "maxTokens": 30,
                "temperature": 0.5,
                "topP": 0.9,
                "stopSequences": ["User:"]
            },
            additionalModelRequestFields={}
        )

        # Parse and return the response
        return response["output"]["message"]["content"][0]["text"]
    
    except Exception as e:
        print(f"Error invoking Bedrock model: {e}")
        return None

def main():

    conversation = []
    print("Chatbot: Hello! How can I assist you today?😑")

    # keep asking for input, till user exit
    while True:

        prompt = input("User: ")
        if prompt == "exit":
            print("Goodbye human friend 😶‍🌫️")
            break
        
        # append query
        conversation.append({
                "role": "user",
                "content": [{"text": prompt}]
            })
        response = invoke_chat_bot(conversation)
        
        if response:
            print("Response from Bedrock model: " + response)
            # append response
            conversation.append({
                "role": "assistant",
                "content": [{"text": response}]
            })
        else:
            print("Failed to get a response from the Bedrock model.")

if __name__ == "__main__":
    main()