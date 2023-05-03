from pathfinder.ai.ai import LanguageModel

class Azure(LanguageModel):

    def configure(self, api_key: str) -> str:
        """Configure the OpenAI Access"""

        return api_key
