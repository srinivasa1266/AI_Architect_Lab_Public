def chatbot_response(user_input: str) -> str:
    # Starter logic for local experimentation.
    return f"AI Response: {user_input}"

if __name__ == "__main__":
    while True:
        user = input("You: ")
        if user.lower().strip() in {"exit", "quit"}:
            break
        print(chatbot_response(user))
