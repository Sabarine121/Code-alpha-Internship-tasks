def chatbot():
    print("🤖 Welcome to SmartBot! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("SmartBot: Hello! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("SmartBot: I'm doing well, thank you! 😊")
        elif user_input in ["what is your name", "who are you"]:
            print("SmartBot: I'm SmartBot, your friendly assistant.")
        elif user_input in ["what can you do", "help me"]:
            print("SmartBot: I can chat with you, tell you the time, give fun facts, and more!")
        elif user_input in ["tell me a joke", "joke"]:
            print("SmartBot: Why don't scientists trust atoms? Because they make up everything! 😄")
        elif user_input in ["what is the time", "time"]:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"SmartBot: The current time is {current_time}.")
        elif user_input in ["who created you", "who made you"]:
            print("SmartBot: I was created by a curious coder like you!")
        elif user_input in ["thank you", "thanks"]:
            print("SmartBot: You're welcome! 😊")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("SmartBot: Goodbye! Have a great day! 👋")
            break
        else:
            print("SmartBot: I'm not sure how to respond to that. Can you try something else?")
chatbot()