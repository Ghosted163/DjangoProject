from django.shortcuts import render

def index(request):
    return render(request, 'index.html')        # ← drop the "polls/" prefix

def checkout(request):
    return render(request, 'checkout.html')

def completion(request):
    return render(request, 'completion.html')
