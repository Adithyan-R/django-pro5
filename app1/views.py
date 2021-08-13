from django.shortcuts import render

# Create your views here.
def app1home(request):
    return render(request,'first.html')

