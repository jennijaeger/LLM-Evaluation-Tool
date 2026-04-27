import os
from dotenv import load_dotenv

load_dotenv()


# -------- GPT --------

class GPTClient:

    def __init__(self):
        from openai import OpenAI

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.name = "gpt"

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content


# -------- Claude --------

class ClaudeClient:

    def __init__(self):
        from anthropic import Anthropic

        self.client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        self.name = "claude"

    def generate(self, prompt):

        response = self.client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        return response.content[0].text


# -------- Gemini --------

class GeminiClient:

    def __init__(self):
        from google import genai

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.name = "gemini"

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text


# -------- Helper --------

def get_all_clients():

    return [
        GPTClient(),
        ClaudeClient(),
        GeminiClient()
    ]