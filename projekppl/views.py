from django.shortcuts import render

def splash(request):
    return render(request, 'splash.html')
def home(request):
    return render(request,'index.html')
def translasi(request):
    return render(request,'translasi.html')