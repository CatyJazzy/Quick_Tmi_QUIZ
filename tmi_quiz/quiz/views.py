from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def question(request, question_id):
    return render(request, 'q{0}.html'.format(question_id))

def login(request):
    return render(request, 'nickname.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def scoring(request):
    return render(request, 'scoring.html')

def result(request):
    return render(request, 'result.html')