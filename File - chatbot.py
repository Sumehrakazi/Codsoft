def chatbot():
    print("Welcome to Simple Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "hi" or user_input == "hello":
            print("Chatbot: Hello! How can I assist you today?")
        
        elif user_input == "how are you?":
            print("Chatbot: I'm just a program, but I'm doing well! How about you?")
        
        elif user_input == "what is your name?":
            print("Chatbot: I'm SimpleBot, here to help you.")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif user_input == "exit":
            print("Chatbot: Exiting... Goodbye!")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
