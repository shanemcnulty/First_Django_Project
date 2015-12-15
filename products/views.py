from django.shortcuts import render
from accounts.models import Magazine


def magazines(request):
    args = {'magazines': Magazine.objects.all()}
    return render(request, 'magazines.html', args)
