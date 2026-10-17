# CodeAlpha_Chatbot

A simple rule-based chatbot written in Python, built as **Task 4** of the CodeAlpha Python Programming Internship.

## What it does

You type a message and the chatbot replies using a set of fixed rules. It keeps chatting until you say goodbye.

## What it understands

| You type | Chatbot replies |
|----------|-----------------|
| `hello`, `hi`, `hey` | Hi! |
| `how are you` | I'm fine, thanks! |
| `what is your name`, `who are you` | I'm a simple chatbot built with Python. |
| `what can you do`, `help` | A short list of things to try |
| `thanks`, `thank you` | You're welcome! |
| `bye`, `goodbye`, `exit` | Goodbye! (and the chat ends) |
| anything else | A polite message saying it doesn't understand |

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if you don't have it.
2. Download `chatbot.py` from this repository.
3. Open a terminal in the folder with the file and run:

```
python chatbot.py
```

## Example chat

```
Chatbot: Hi! I'm a simple chatbot. Type 'bye' to leave.
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks!
You: bye
Chatbot: Goodbye!
```

## Concepts used

`if-elif-else` conditions, functions, `while` loops, and user input/output.

## Ideas to improve it

- Add more questions and answers
- Make it recognize keywords inside longer sentences
- Add the current time or date as a reply

## Author

Made by Yasin as part of the CodeAlpha Python Programming Internship.
