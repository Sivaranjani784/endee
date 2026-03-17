import google.generativeai as genai

# 🔑 Add your API key here
genai.configure(api_key="AIzaSyCgEk5YbBrvbqgUlkwVvqvxOiyi4Vp8nlg")

model = genai.GenerativeModel("gemini-pro")

# Load data
def load_data():
    with open("data.txt", "r") as f:
        return f.readlines()

# Simple search (Endee concept simulation)
def search(query, data):
    results = []
    for line in data:
        if any(word in line.lower() for word in query.lower().split()):
            results.append(line)
    return " ".join(results)

data = load_data()

print("🤖 AI Chatbot (RAG) - type 'exit' to stop")

while True:
    query = input("You: ")
    
    if query.lower() == "exit":
        break

    context = search(query, data)

    prompt = f"""
    Answer the question based on this context:
    {context}

    Question: {query}
    """

    response = model.generate_content(prompt)
    
    print("Bot:", response.text)
