from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect,render

from .models import Machine
# Create your views here.
def home(request):
    return render(request, "index.html")

@login_required
def scan(request, token):
    get_object_or_404(Machine, qr_token=token)
    return redirect("home")