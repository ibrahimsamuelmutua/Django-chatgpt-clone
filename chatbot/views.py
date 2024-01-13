from django.shortcuts import render
from django.http import JsonResponse
import openai

open_ai_key = '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'
openai.api_key = open_ai_key


# Create your views here.

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choice[0]


def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hi this is my response'
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html')
