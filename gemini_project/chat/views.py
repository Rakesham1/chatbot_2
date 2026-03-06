from django.shortcuts import render
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_view(request):
    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=question
        )

        answer = response.text

    return render(request, "chat/index.html", {"answer": answer})