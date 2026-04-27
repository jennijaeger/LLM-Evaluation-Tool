import os
from dotenv import load_dotenv

load_dotenv()

# -------- GPT --------
def test_openai():
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Sag Hallo"}],
    )

    print("GPT Antwort:")
    print(response.choices[0].message.content)


# -------- Claude --------
def test_claude():
    from anthropic import Anthropic
    import os

    client = Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=50,
        messages=[
            {"role": "user", "content": "Sag Hallo"}
        ],
    )

    print("\nClaude funktioniert:")
    print(response.content[0].text)


# -------- Gemini --------
def test_gemini():
    from google import genai
    import os

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents="Sag Hallo"
    )

    print("\nGemini funktioniert:")
    print(response.text)


if __name__ == "__main__":
    test_openai()
    test_claude()
    test_gemini()