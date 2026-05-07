def chatbot_reply(user_text):
    text = user_text.lower()

    if "hello" in text or "hi" in text:
        return "Hello 👋 I am Fake News Assistant."

    elif "fake news" in text:
        return "Fake news means false or misleading information shown as real."

    elif "real news" in text:
        return "Real news usually comes from trusted and verified sources."

    elif "how detect" in text:
        return "I use Machine Learning and NLP to classify news."

    elif "why fake" in text:
        return "Because it may contain unrealistic claims or suspicious words."

    elif "thank" in text:
        return "You're welcome 😊"

    else:
        return "Ask me about fake news, real news, or detection system."