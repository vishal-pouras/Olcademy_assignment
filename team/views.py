from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Team
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView


def teams(request):
    all_teams = Team.objects.all()                          # get the list of all Team objects
    context = {'all_teams': all_teams}
    return render(request, 'team/teams.html', context)


def login(request):
    return render(request, 'team/login.html')


class TeamListView(ListView):
    model = Team


class TeamCreate(CreateView):
    model = Team
    fields = ['teamname', 'member1', 'email1', 'contact1', 'member2', 'email2', 'contact2', 'member3', 'email3', 'contact3']
    success_url = reverse_lazy('team-list')


class TeamUpdate(UpdateView):
    model = Team
    fields = ['teamname', 'member1', 'email1', 'contact1', 'member2', 'email2', 'contact2', 'member3', 'email3', 'contact3']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('team-list')