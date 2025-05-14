from fastapi import Body
from typing import Union, List
from langchain.prompts.chat import ChatPromptTemplate
from utils.history import History

# def create_models_chains(history, history_len, prompts, models, tools, callbacks, conversation_id, metadata):
#     memory = None
#     chat_prompt = None

#     if history:
#         history = [History.from_data(h) for h in history]
#         input_msg = History(role="user", content=prompts["llm_model"]).to_msg_template(
#             False
#         )
#         chat_prompt = ChatPromptTemplate.from_messages(
#             [i.to_msg_template() for i in history] + [input_msg]
#         )
#     elif conversation_id and history_len > 0:
#         memory = ConversationBufferDBMemory(
#             conversation_id=conversation_id,
#             llm=models["llm_model"],
#             message_limit=history_len,
#         )
#     else:
#         input_msg = History(role="user", content=prompts["llm_model"]).to_msg_template(
#             False
#         )
#         chat_prompt = ChatPromptTemplate.from_messages([input_msg])

#     if "action_model" in models and tools:
#         llm = models["action_model"]
#         llm.callbacks = callbacks
#         agent_executor = agents_registry(
#             llm=llm, callbacks=callbacks, tools=tools, prompt=None, verbose=True
#         )
#         full_chain = {"input": lambda x: x["input"]} | agent_executor
#     else:
#         llm = models["llm_model"]
#         llm.callbacks = callbacks
#         chain = LLMChain(prompt=chat_prompt, llm=llm, memory=memory)
#         full_chain = {"input": lambda x: x["input"]} | chain
#     return full_chain

async def file_chat_api(
        question: str = Body(..., description="问题"),
        file_path :  Union[List,str] = Body([], description="文件地址")):
    
    chain = get_chain()
