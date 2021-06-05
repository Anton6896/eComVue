from urllib.request import Request

from django.shortcuts import render


def profile_home_view(request):
    """
    this is the hello page of Django server
    """

    context = {
        "url": get_current_host(request)
    }
    return render(request, 'profile/home.html', context)


def get_current_host(request: Request) -> str:
    scheme = request.is_secure() and "https" or "http"
    return f'{scheme}://{request.get_host()}/'
