from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import json
from flask import jsonify

app = Flask(__name__)

# Initialize the Bedrock runtime client
client = boto3.client(service_name='bedrock-runtime', region_name='ap-south-1')
model_id = "amazon.titan-text-express-v1"

def invoke_chat_bot(conversation, model_id='amazon.titan-text-express-v1'):
    try:
        # return "Hi"
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
    
@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    conversation = data['conversation']
    user_message = data['message']

    conversation.append({
        "role": "user",
        "content": [{"text": user_message}]
    })
    
    response = invoke_chat_bot(conversation)
    print(response)

    if response:
        conversation.append({
            "role": "assistant",
            "content": [{"text": response}]
        })
        return jsonify({"message": response, "conversation": conversation})
    else:
        return jsonify({'error': 'Failed to get a response from the Bedrock model.'}), 500
    
if __name__=='__main__':
    app.run(debug=True)
