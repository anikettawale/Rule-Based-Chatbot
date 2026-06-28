print("=" * 50)
print("🤖 Welcome to CodSoft Rule-Based Chatbot")
print("Type 'bye' to exit.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is CodBot.")

    elif user == "who created you":
        print("Bot: I was created by Aniket Tawale for the CodSoft AI Internship.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
