
import re

print("===== CHATBOT ASSISTANT =====")
print("Hello! Welcome to our support chatbot.")
print("Ask me about business hours, products, or help.")
print("Type 'bye' to exit.")

while True:
    user = input("\nYou: ").lower().strip()

    if re.search(r"\b(bye|exit|quit)\b", user):
        print("Bot: Thank you! Have a nice day!")
        break

    elif re.search(r"\b(hi|hello|hey)\b", user):
        print("Bot: Hello! How can I help you?")

    elif "hours" in user or "timing" in user:
        print("Bot: Our business hours are 9 AM to 6 PM.")

    elif "price" in user or "product" in user:
        print("Bot: Please check our product list for prices.")

    elif "help" in user or "support" in user:
        print("Bot: Sure! Tell me your problem.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    else:
        print("Bot: Sorry, I didn't understand. Please try again.")
