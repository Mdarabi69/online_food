from django.shortcuts import render, HttpResponse


def register(request):
    return render(request, 'accounts/register.html')
