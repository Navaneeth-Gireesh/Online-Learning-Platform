from django.shortcuts import render, redirect
import random
# Create your views here.

# Base Page
def base(request):
    return render(request, 'core_app/base.html')

# Landing Page
def index(request):
    if request.user.is_authenticated:
        return redirect('user_languages_view')
    return render(request, 'core_app/index.html')

# Error Page
def error_404(request):

    error_pages = ['core_app/Error_404/1.error.html', 'core_app/Error_404/2.error.html',
                    'core_app/Error_404/3.error.html', 'core_app/Error_404/4.error.html',
                    'core_app/Error_404/5.error.html']

    selected_page = random.choice(error_pages)

    return render(request, selected_page)


# Custom Handlers Exceptions
def custom_404(request, exception):

    error_pages = ['core_app/Error_404/1.error.html', 'core_app/Error_404/2.error.html',
                    'core_app/Error_404/3.error.html', 'core_app/Error_404/4.error.html',
                    'core_app/Error_404/5.error.html']

    selected_page = random.choice(error_pages)

    return render(request, selected_page, status=404)