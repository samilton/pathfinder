from pathfinder.ai.ai import LanguageModel


class OpenAI(LanguageModel):
    def configure(self, api_key: str) -> str:
        return api_key
