import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .services import answer_question

def home(request): return render(request,"chatbot/index.html")

@require_POST
def chat(request):
    try: data=json.loads(request.body)
    except json.JSONDecodeError: return JsonResponse({"error":"Invalid request."},status=400)
    message=str(data.get("message","")).strip()
    if not message: return JsonResponse({"error":"Please enter a question."},status=400)
    return JsonResponse(answer_question(message))
