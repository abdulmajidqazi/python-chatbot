import requests

print("🤖 Python ChatBot")

print("To end the chat, type 'exit'.\n")

while True:
    prompt = input("👤 You: ")

    if prompt.lower() == "exit":
        print("Thank you for using Python ChatBot.")
        break

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    print(f"\n🤖 AI: {result['response']}\n")