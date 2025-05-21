# Simple rule-based chatbot by Zeenat
print("Welcome to Zeenat's Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ").lower()  # Get user input and convert to lowercase
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hi there! How can I help you?")
    elif "name" in user_input:
        print("Chatbot: I'm Zeenat's awesome chatbot! What's your name?")
    elif "how are you" in user_input:
        print("Chatbot: I'm doing great, thanks for asking!")
    elif "what is ai" in user_input:
        print("Chatbot: AI is like me—smart tech that thinks and responds! Want to know more?")
    elif "coding" in user_input:
        print("Chatbot: Coding is like teaching a computer to think—fun, right? Want tips?")
    else:
        print("Chatbot: Sorry, I don’t understand. Try saying 'hello', 'name', or 'what is AI'!")