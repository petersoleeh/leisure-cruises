from django.shortcuts import render

# Create your views here.
#landing page
def index(request):
    return render(request,'index.html')
