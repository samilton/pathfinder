from typing import Protocol


class LanguageModel(Protocol):
    def __init__(self):
        self.name = "Ai"

    def configure(api_key: str) -> int:
        return api_key


class OpenAI:
    def configure(self, api_key: str) -> str:
        return api_key


if __name__ == "__main__":
    a = OpenAI()
    api_key = a.configure("xyx")
    print(api_key)
