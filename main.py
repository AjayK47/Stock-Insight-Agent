import autogen

# Configure the agents
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-4o-mini"],
    },
)

# Configure the LLM
llm_config = {
    "config_list": config_list,
    "timeout": 120
}

company = input("Enter Company Name: ")

financial_tasks = [
    f"""What are the current stock prices of {company}, and how is the performance over the past month in terms of percentage change?""",
    """Investigate possible reasons for the stock performance leveraging market news. Use the following code snippet:
    ```python
    from duckduckgo_search import DDGS
    results = DDGS().news(topic, max_results=8)
    print(results)
    ```
    to retrieve news article data.""",
]

Financial_epert_task = [
    """Give your opinion on the immediate future of given company stocks: growth, decline, or stagnation."""
]

financial_assistant = autogen.AssistantAgent(
    name="Financial_assistant",
    llm_config=llm_config,
)
research_assistant = autogen.AssistantAgent(
    name="Researcher",
    llm_config=llm_config,
)
Financial_expert = autogen.AssistantAgent(
    name="Financial_expert",
    llm_config=llm_config,
    system_message="""
        You are a professional Financial investement predictor, known for
        your excellent Stock predictions Skills.
        You Undesrtand Company news and Past Changes in stocks to Predict , if company will show immediate growth or decline in stocks.
        Reply "TERMINATE" in the end when everything is done.
        """,
)

user_proxy_auto = autogen.UserProxyAgent(
    name="User_Proxy_Auto",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "tasks",
        "use_docker": False,
    },  
)
user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "tasks",
        "use_docker": False,
    },  
)


chat_results = autogen.initiate_chats(
    [
        {
            "sender": user_proxy_auto,
            "recipient": financial_assistant,
            "message": financial_tasks[0],
            "clear_history": True,
            "silent": False,
            "summary_method": "last_msg",
        },
        {
            "sender": user_proxy_auto,
            "recipient": research_assistant,
            "message": financial_tasks[1],
            "max_turns": 4,  
            "summary_method": "reflection_with_llm",
        },
        {
            "sender": user_proxy,
            "recipient": Financial_expert,
            "message": Financial_epert_task[0],
            "carryover": "I want to include a figure or a table of data in the blogpost.",  
        },
    ]
)

