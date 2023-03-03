from django.shortcuts import render


# Create your views here.
def loginGoogle(request):
    return render(request, 'loginGoogle.html', {})

