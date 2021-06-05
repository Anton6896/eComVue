from django.shortcuts import render


def profile_home_view(request):
    """
    this is the hello page of Django server
    """
    return render(request, 'profile/home.html')
