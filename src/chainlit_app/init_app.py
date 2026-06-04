from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from abstract.llm_manager import LLMManager
from models.llm import LLMName


def register_llm_managers():
    LLMManager.register(LLMName.LAPA, ChatOpenAI)
    LLMManager.register(LLMName.OPENAI, ChatOpenAI)
    LLMManager.register(LLMName.ANTHROPIC, ChatAnthropic)
    LLMManager.register(LLMName.GOOGLE, ChatGoogleGenerativeAI)
