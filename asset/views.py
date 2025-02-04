from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def overview(request):
    return render(request, 'asset/overview.html')