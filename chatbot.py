from google import genai

client = genai.Client(api_key="your_api_key")

def chatbot_reply(user_text):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_text
    )

    return response.text