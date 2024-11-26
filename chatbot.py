import random
import re

class SimpleChatbot:
    def __init__(self):
        # Dictionary of predefined responses
        self.responses = {
            r'hi|hello|hey': [
                "Hello there!",
                "Hi! How are you today?",
                "Greetings! What can I help you with?"
            ],
            r'how are you': [
                "I'm doing great, thanks for asking!",
                "I'm well, how about you?",
                "Feeling good and ready to chat!"
            ],
            r'what\'?s your name': [
                "I'm a simple chatbot.",
                "You can call me ChattyBot.",
                "I'm an AI assistant created to chat with you!"
            ],
            r'bye|goodbye': [
                "Goodbye!",
                "See you later!",
                "Have a great day!"
            ],
            r'help': [
                "I can chat about various topics. Just talk to me!",
                "I'm here to help. What would you like to discuss?",
                "Ask me anything, and I'll do my best to respond."
            ],
            r'weather': [
                "I can't actually check the weather, but I hope it's nice where you are!",
                "Weather chat? I'd love to, but I'm just a simple chatbot.",
                "Sunny or rainy, I'm always here to chat!"
            ]
        }

        # Fallback responses for when no pattern matches
        self.fallback_responses = [
            "I'm not sure how to respond to that.",
            "Could you rephrase that?",
            "That's interesting, but I don't quite understand.",
            "I'm still learning. Can you explain that differently?"
        ]

    def get_response(self, user_input):
        """
        Generate a response based on the user's input.

        Args:
            user_input (str): The message from the user

        Returns:
            str: The chatbot's response
        """
        # Convert input to lowercase
        user_input = user_input.lower()

        # Check for matching patterns
        for pattern, response_list in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(response_list)

        # If no pattern matches, return a fallback response
        return random.choice(self.fallback_responses)

    def chat(self):
        """
        Start an interactive chat session with the user.
        """
        print("Chatbot: Hello! Type 'bye' to exit.")

        while True:
            try:
                user_input = input("You: ").strip()

                # Exit condition
                if user_input.lower() in ['bye', 'goodbye', 'exit']:
                    print("Chatbot: " + random.choice(self.responses[r'bye|goodbye']))
                    break

                # Get and print response
                response = self.get_response(user_input)
                print("Chatbot:", response)

            except (KeyboardInterrupt, EOFError):
                print("\nChatbot: Goodbye!")
                break


def main():
    chatbot = SimpleChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()