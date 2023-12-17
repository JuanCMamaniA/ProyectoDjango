from django.shortcuts import render
def casa(request):
    return render(request, 'index.html')

def venta_auto(request):
    return render(request, 'pages/venta_auto.html')