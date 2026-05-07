📰 Fake News Detection + Chatbot

Fake News Detection + Chatbot is a Machine Learning and Natural Language Processing (NLP) based web application that classifies news articles or headlines as Fake or Real using supervised learning techniques. The project also includes an AI-powered chatbot built with Gemini API and an interactive Streamlit user interface.

🚀 Features
Fake vs Real News Prediction
NLP-based Text Preprocessing
TF-IDF Feature Extraction
Machine Learning Classification
AI Chatbot Integration
Real-time Prediction System
Interactive Streamlit Web App
Dashboard Analytics
Confidence Score Display
🛠️ Tech Stack
Programming Language
Python
Machine Learning & Data Processing
Scikit-learn
Pandas
NumPy
Natural Language Processing
TF-IDF Vectorizer
Regular Expressions (Regex)
Web Framework
Streamlit
AI Chatbot
Google Gemini API
google-genai
Model Used
Logistic Regression
📂 Project Structure
fake_news_project/
│── app.py
│── chatbot.py
│── train_model.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
⚙️ Installation

Clone the repository:

git clone YOUR_REPOSITORY_LINK

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
🤖 Gemini API Setup
Create API key from:

Google AI Studio

Add your API key inside chatbot.py
client = genai.Client(api_key="YOUR_API_KEY")
📌 Project Workflow
Data Collection
Text Preprocessing
TF-IDF Feature Extraction
Machine Learning Model Training
Fake News Prediction
AI Chatbot Response Generation
Streamlit Deployment
🎯 Project Objective

The main objective of this project is to identify misleading or false news content using Machine Learning techniques and provide users with an intelligent interactive platform for analyzing and verifying news articles.

🌐 Deployment

This project can be deployed using:

Streamlit Community Cloud
GitHub
📜 License

This project is developed for educational and learning purposes.
