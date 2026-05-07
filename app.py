import streamlit as st
import pickle
import re
import numpy as np
import pandas as pd

from chatbot import chatbot_reply

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide"
)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def predict_news(news):
    cleaned = clean_text(news)
    vec = vectorizer.transform([cleaned])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]

    result = "REAL NEWS ✅" if pred == 1 else "FAKE NEWS ❌"
    confidence = round(np.max(prob) * 100, 2)

    return result, confidence

st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Select", [
    "Home",
    "Detect News",
    "Chatbot",
    "Dashboard"
])


if page == "Home":
    st.title("📰 Fake News Detection + Chatbot")
    st.write("Detect whether news is Fake or Real using Machine Learning.")


elif page == "Detect News":
    st.title("🧠 Fake News Detector")

    news = st.text_area("Paste headline or article:")

    if st.button("Predict"):
        if news.strip() == "":
            st.warning("Please enter text.")
        else:
            result, conf = predict_news(news)

            st.success(result)
            st.progress(int(conf))
            st.write(f"Confidence: {conf}%")


elif page == "Chatbot":
    st.title("💬 Chatbot")

    user_msg = st.text_input("Ask anything:")

    if st.button("Send"):
        if user_msg.strip():
            reply = chatbot_reply(user_msg)

            st.write("🧑 You:", user_msg)
            st.write("🤖 Bot:", reply)

elif page == "Dashboard":
    st.title("📊 Dashboard")

    df = pd.read_csv("fake_news.csv")

    st.dataframe(df)

    real_count = len(df[df["label"] == 1])
    fake_count = len(df[df["label"] == 0])

    chart = pd.DataFrame({
        "Type": ["Real", "Fake"],
        "Count": [real_count, fake_count]
    })

    st.bar_chart(chart.set_index("Type"))