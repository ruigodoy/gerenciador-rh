from django.shortcuts import render

<<<<<<< HEAD
from django.contrib.auth.decorators import login_required

@login_required
=======

>>>>>>> 9c9ea1061fa0b62b4203d85bdb7e0b97052cadd9
def home(request):
    return render(request, 'core/index.html')
