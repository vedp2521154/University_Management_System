import sys
import time

from graph.builder import app


def print_delayed(text: str, delay: float = 0.015):
    """Print text with a ChatGPT-like typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():

    print("=" * 50)
    print("      UNIVERSITY MANAGEMENT ASSISTANT")
    print("=" * 50)

    name = input("\nEnter your name: ").strip().title()

    if not name:
        name = "Student"

    welcome_message = f"""
Welcome, {name}!

I can help you with:
• Admissions
• Exams
• Fees
• Scholarships

Type 'help' for assistance.
Type 'exit' to quit.
"""

    print_delayed(welcome_message, delay=0.01)

    conversation_history = []

    while True:

        query = input(f"{name} > ").strip()

        if not query:
            continue

        if query.lower() == "exit":
            print("\nThank you for using the University Management Assistant.")
            print("Goodbye!")
            break

        if query.lower() == "help":

            print("\nYou can ask questions like:\n")
            print("• How do I take admission?")
            print("• What are the exam dates?")
            print("• Tell me about fees")
            print("• Scholarship details")
            print()

            continue

        state = {
            "user_query": query,
            "intent": "",
            "response": "",
            "history": conversation_history,
            "user_name": name,
        }

        print("\nAssistant is thinking...\n")

        result = app.invoke(state)

        conversation_history.append(f"User: {query}")
        conversation_history.append(f"Assistant: {result['response']}")

        print("\nAssistant:\n")
        print_delayed(result["response"], delay=0.01)

        print("-" * 50)


if __name__ == "__main__":
    main()