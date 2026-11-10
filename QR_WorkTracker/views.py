from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.cache import never_cache

from . import qr
from .models import Machine

def home(request):
    return render(request, "index.html")

@staff_member_required
def qr_display(request,code):
    machine = get_object_or_404(Machine, code=code)
    return render(request, "qr.html", {"machine": machine})

@staff_member_required
@never_cache
def qr_image(request, code):
    machine = get_object_or_404(Machine, code=code)
    url = settings.PUBLIC_BASE_URL + reverse("scan", args=[qr.create_token(machine)])
    return HttpResponse(qr.render_svg(url), content_type="image/svg+xml")

@login_required
def scan(request, token):
    code = token.split(":",1)[0]
    machine = get_object_or_404(Machine, code=code)
    if not qr.verify_token(machine, token):
        return HttpResponseForbidden("Invalid or expired QR code.")
    return redirect("home")