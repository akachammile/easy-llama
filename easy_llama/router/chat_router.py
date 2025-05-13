from fastapi import APIRouter, Request
from langchain.callbacks import AsyncIteratorCallbackHandler

chat_router = APIRouter(prefix="/chat", tags=["对话"])

@chat_router.post("/file")
async def file_chat():
    print("Xxxxxxxx")