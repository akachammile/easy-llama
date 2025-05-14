from fastapi import APIRouter, Request
from server.api.chat_api import file_chat_api

chat_router = APIRouter(prefix="/chat", tags=["对话"])



chat_router.post("/file")(file_chat_api)