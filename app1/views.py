from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'yuvraj','age':23}
    return render(request,'first.html',context=d)
