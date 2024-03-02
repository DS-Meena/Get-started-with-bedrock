from langchain import hub

def plain_llm(question):
    template = """Question: {question}
    Let's think step by step.
    Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = Bedrock(
        credentials_profile_name="default",model_id="anthropic.claude-v2", region_name="a-south-1"
    )


