import google.generativeai as genai

# Unga Gemini API key-a inga podunga
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

print("=== Welcome to EduGenie-AI Learning Assistant ===")
print("Type 'exit' to stop.\n")

while True:
    user_query = input("Ask EduGenie: ")
    if user_query.lower() == "exit":
        break
    if not user_query.strip():
        continue
    
    try:
        response = model.generate_content(f"You are EduGenie, an AI learning assistant. Answer briefly: {user_query}")
        print("\nEduGenie Answer:\n" + response.text + "\n" + "-"*40)
    except Exception as e:
        print(f"\nError: {e}\n")