from django.shortcuts import render

def landlords(request):
    return render(request, 'landlords/landlords.html')
