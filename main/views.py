from django.shortcuts import render

# Create your views here.
    
def test (request):
    return render (request,"test.html")

def third(request):
    return render (request, "test3.html")

  



