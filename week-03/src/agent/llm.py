from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from src.settings import settings

llm = OpenAIChatModel(
    settings.OPENAI_MODEL,
    provider=OpenRouterProvider(api_key=settings.OPENROUTER_API_KEY),
)
