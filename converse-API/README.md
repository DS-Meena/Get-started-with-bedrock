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

## Troubleshooting 🔨

### Not able to access FM 🚪

```
Error invoking Bedrock model: An error occurred (AccessDeniedException) when calling the InvokeModel operation: You don't have access to the model with the specified model ID.
Failed to get a response from the Bedrock model.
```

1. `aws sts get-caller-identity` Use this to know current user.
2. Stupid! 😑 I was using wrong aws region in the code. In the configuration file it was correct but remember to check code also.