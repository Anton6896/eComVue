from django.shortcuts import render


# Create your views here.
def profile_home_view(request):
    return render(request, 'profile/home.html')
