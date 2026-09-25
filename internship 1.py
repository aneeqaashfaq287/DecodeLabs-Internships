responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hello! How can I help you?",
    "how are you": "I am doing great!",
    "what is your name": "I am a rule-based AI chatbot.",
    "what can you do": "I can answer simple questions.",
    "help": "You can say hello, ask my name, or ask how I am.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "bye": "Goodbye!"
}

print("Bot: Hello! I am your AI chatbot.")
print("Bot: Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(clean_input, "Sorry, I don't understand.")
    print("Bot:", reply)