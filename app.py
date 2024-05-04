import streamlit as st
from g4f.client import Client

def chat_with_bot(messages):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_response = response.choices[0].message.content.replace("Microsoft Copilot", "").strip()
    return bot_response

def main():
    st.title("Owrell V1")

    messages = [
        {"role": "system", "content": "Your name is Owrell and you are an AI model created by OwrellAI."},
        {"role": "system", "content": "Speak the language of the user. Examples: Olá! Qual é seu nome? - Speak Portuguese ; Hello! What is your name? - Speak English"},
    ]

    user_input = st.text_area("You:")
    send_button = st.button("Send")
    
    if send_button:
        if user_input.lower() == "sair":
            st.stop()

        messages.append({"role": "user", "content": user_input})
        bot_response = chat_with_bot(messages)
        st.text_area("Owrell:", value=bot_response, height=200)

if __name__ == "__main__":
    main()
