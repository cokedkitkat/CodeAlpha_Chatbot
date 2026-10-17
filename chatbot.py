"""
CodeAlpha Task 4: Basic Rule-Based Chatbot
------------------------------------------
The chatbot looks at what you type and replies using simple rules.
Type 'bye' to end the chat.
"""


def get_reply(user_message):
    """Look at the user's message and return the matching reply."""
    message = user_message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("what is your name", "who are you"):
        return "I'm a simple chatbot built with Python."
    elif message in ("what can you do", "help"):
        return "I can chat about a few things. Try: hello, how are you, thanks, or bye."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Try 'hello' or 'how are you'."


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to leave.")

    # Keep chatting until the user says bye
    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        print("Chatbot:", reply)

        if user_message.lower().strip() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    chat()
