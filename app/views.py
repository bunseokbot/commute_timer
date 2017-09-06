"""View of commute_timer."""
from django.shortcuts import render


def index(request):
    """Index page."""
    return render(request, 'app/index.html')
