from typing import Dict, List, Tuple, Union
from langchain.prompts.chat import ChatMessagePromptTemplate
from pydantic import BaseModel, Field



class History(BaseModel):
    """生成对话历史
    """
    role: str = Field(...)
    content: str = Field(...)

    
    def msg_to_template(self):
        return ChatMessagePromptTemplate.from_template(self.content)


    
