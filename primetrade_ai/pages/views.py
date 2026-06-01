from django.shortcuts import render




def auto_auth_page(request):

    return render(request, 'loading_page.html')

def signup_page(request):
    return render(request, 'signup_page.html')

def login_page(request):
    return render(request, 'login_page.html')
