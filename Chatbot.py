# Define some predefined rules and responses
rules = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm just a computer program, but I'm here to assist you. How can I help?",
    "what is your name": "I'm just a chatbot, so I don't have a name.",
    "ok":"Anything Else...",
    "Thank you":"I,m happy to help.",
    "bye": "Goodbye! If you have more questions in the future, feel free to ask."
}

# Function to process user input and provide responses
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    # Check if the user input matches any of the predefined rules
    for rule, response in rules.items():
        if rule in user_input:
            return response

    # If no match is found, provide a default response
    return "I'm not sure how to respond to that. Please ask me something else."

# Main conversation loop
print("Chatbot: Hello! How can I assist you today? Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)
