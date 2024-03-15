from langchain import hub
from langchain.prompts import PromptTemplate
from langchain_community.llms import Bedrock
from langchain.chains import LLMChain
from langchain.agents import tool, Tool, create_react_agent, AgentExecutor

@tool
def sum_list(string_list_of_nums: str) -> int:
    """Takes an python string containing a list of numbers, converts them to ints and sum them all together to provide a total."""
    # firstly lets make sure we are working with int
    string_list_of_nums = string_list_of_nums.replace("[", "")
    string_list_of_nums = string_list_of_nums.replace("]", "")
    string_list_of_nums = string_list_of_nums.split(", ")

    # convert list of strings into list of ints
    list_nums = list(map(int, string_list_of_nums))
    print(list_nums)

    for i in range(len(list_nums)):
        list_nums[i] = int(list_nums[i])
    return sum(list_nums)

def llm_with_tools(question):
    prompt = hub.pull("hwchase17/react-chat")

    sum_tool = Tool(
        name="sum_tool",
        func=sum_list,
        description="useful for adding numbers"
    )
    tools = [sum_tool]

    llm = Bedrock(
        credentials_profile_name="default",model_id="amazon.titan-text-lite-v1", region_name="us-west-2"
    )

    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    answer = agent_executor.invoke({
        "input": f"{question}. Only use a use tool if need, otherwise respond with final answer.", 
        "chat_history": "",
        # "prompt_override": {
        #     "maximum_length": 100,
        #     "stop_sequences": ["."]
        # }
    })

    print(answer["output"])

def plain_llm(question):
    template = """Question: {question}
    Let's think step by step.
    Answer:
    """

    # no to create the perfect json body
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = Bedrock(
        credentials_profile_name="default",model_id="amazon.titan-text-lite-v1", region_name="us-west-2"
    )
    
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    print(llm_chain.invoke(question))

def main():

    # Ask a question
    # question = "Can I get a job in Amazon"
    # plain_llm(question)

    # Ask the text model to do summation
    list_of_nums = [645, 6, 2, 9, 2]
    question = f"Sum of the following numbers: {list_of_nums}"  
    # plain_llm(question)     

    # expected_sum = sum(list_of_nums)
    # print(f"\nExpected sum: {expected_sum}") 

    """
        plain llm can'get give you the correct summation.
    """
    llm_with_tools(question)
    expected_sum = sum(list_of_nums)
    print(f"\nExpected sum: {expected_sum}")

main()