# Converse API 🗣️

In this program, we will try to start a conversation with one of the Foundation models using bedrock converse API.

## Get Access of FM 🔐

First you need to get access of one the foundation models before able to access it.

1. Got to Amazon Bedrock service -> Bedrock configurations -> Model access 
2. Click on available to request -> submit.
3. Sometimes they are approved automatically and othertimes manually. 

You need access to the Bedrock FM.

### Titan Text G1 - Express 🚅

Model Id: `amazon.titan-text-express-v1`

**API Request Format:**

```
{
 "modelId": "amazon.titan-text-express-v1",
 "contentType": "application/json",
 "accept": "application/json",
 "body": "{\"inputText\":\"this is where you place your input text\",\"textGenerationConfig\":{\"maxTokenCount\":8192,\"stopSequences\":[],\"temperature\":0,\"topP\":1}}"
}
```

Rembember, to use correct request format while trying to get response from Amazon Bedrock.

## Create a conversational web app 🏪

We are able to send one request and one response, now we want to record the chat history. Recording chat history is necessary for a chat bot.

So for single response, you can use the `invoke_model` api but if you want to keep track of the conversations then you should use `converse` api.

Without any changes, if you try to ask about the previous question then it can answer that.
```bash
User: what is the capital of India?
Response from Bedrock model:

The capital of India is New Delhi. It is the seat of the Government of India and the home of the President. 
User: what was the first question?
Response from Bedrock model:

I am not able to remember previous conversations I've had with customers due to my programming and limitations in artificial intelligence. However, I'm here to
User: 
```

We need to append the request and response in the conversation list.

```bash
Chatbot: Hello! How can I assist you today?😑
User: what is the capital of dubai?
Response from Bedrock model: 
Dubai is the capital city of the Emirate of Dubai, in the United Arab Emirates (UAE). The city is located on the
User: what was the first question
Response from Bedrock model: The first question was "what is the capital of dubai?".
User: exit
Goodbye human friend 😶‍🌫️
```

But this seems expensive, maybe not. At client side or server side it has to maintain the chat history in some struct. 🤔

The chat-bot can be optimized by 💽:

- **Sliding window approach:** Instead of maintaing all of the conversation, maintain only the most recent N messages. This helps manage token limits and memory usage.

- **Summarization Technique:** Periodically summarize older parts of the conversation to maintain context while reducing token count.

## Troubleshooting 🔨

### Not able to access FM 🚪

```
Error invoking Bedrock model: An error occurred (AccessDeniedException) when calling the InvokeModel operation: You don't have access to the model with the specified model ID.
Failed to get a response from the Bedrock model.
```

1. `aws sts get-caller-identity` Use this to know current user.
2. Stupid! 😑 I was using wrong aws region in the code. In the configuration file it was correct but remember to check code also.