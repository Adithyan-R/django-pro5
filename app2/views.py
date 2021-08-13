from django.shortcuts import render

# Create your views here.
def app2home(request):
    return render(request,'second.html')
