from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def teams(request):
    all_teams = Team.objects.all()
    context = {'all_teams': all_teams}
    return render(request, 'team/admin.html', context)


#def adminpage(request):
