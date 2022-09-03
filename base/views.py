from django.shortcuts import HttpResponse, render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h2>About</h2>')

def contact(request):
    return HttpResponse('<h2>Contact</h2>')