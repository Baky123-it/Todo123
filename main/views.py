from django.shortcuts import render

# Create your views here.
def homepage1 (request):
    return render (request, "test4.html", "test5.html", "test6.html")



def homepage (request):
    return render (request, "index.html")

def test (request):
    return render (request,"test.html")

def third(request):
    return render (request, "test3.html")

  



