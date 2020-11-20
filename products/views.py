from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from votes.models import Votes
from django.utils import timezone


def home(request):
    votedProjects=[]
    projects = Project.objects.all().order_by("-total_votes")
    allVotes = Votes.objects.all()
    for project in projects:
        for vote in allVotes:
            if vote.user == request.user and vote.project == project:
                votedProjects.append(project.id)
    return render(request, 'products/home.html', {"projects": projects, "votedProjects":votedProjects})


def search(request):
    keyword = (request.POST['keyword']).lower()
    all_projects = Project.objects.all()
    projects=[]
    for project in all_projects:
        if keyword in project.title.lower() or project.title.lower() in keyword or keyword in project.sp_framework.lower() or project.sp_framework.lower() in keyword or keyword in project.body.lower() or keyword in project.req_langs.lower() :
            projects.append(project)
    votedProjects=[]
    allVotes = Votes.objects.all()
    for project in projects:
        for vote in allVotes:
            if vote.user == request.user and vote.project == project:
                votedProjects.append(project.id)
    return render(request,'products/home.html', {"projects": projects,"votedProjects":votedProjects})


@login_required
def create(request):
    if request.method == "POST":
        project = Project()
        project.title = request.POST['title']
        project.body = request.POST['body']
        project.req_langs = request.POST['reqLang']
        project.sp_framework = request.POST['spf']
        project.pub_date = timezone.datetime.now()
        project.user = request.user
        project.icon = request.POST['icon']
        project.save()
        return redirect('detail', projectid=project.id)
    else:
        return render(request, 'products/create.html')


def detail(request, projectid):
    votedProject = ''
    project = get_object_or_404(Project, pk=projectid)
    allVotes = Votes.objects.all()
    for vote in allVotes:
            if vote.user == request.user and vote.project == project:
                votedProject = project.id
    return render(request, 'products/projectdetail.html', {"project": project, "votedProject": votedProject})


def upvote1(request, projectid):
    if request.method == "POST":
        project = get_object_or_404(Project, pk=projectid)
        project.total_votes += 1
        vote = Votes(user=request.user, project=project)
        vote.save()
        project.save()
        return redirect('home')


def downvote1(request, projectid):
    if request.method == "POST":
        project = get_object_or_404(Project, pk=projectid)
        project.total_votes -= 1
        allVotes = Votes.objects.all()
        for vote in allVotes:
            if vote.user == request.user and vote.project == project:
                vote.delete()
        project.save()
        return redirect('home')


def upvote2(request, projectid):
    if request.method == "POST":
        project = get_object_or_404(Project, pk=projectid)
        project.total_votes += 1
        vote = Votes(user=request.user, project=project)
        vote.save()
        project.save()
        return redirect('detail', projectid=projectid)


def downvote2(request, projectid):
    if request.method == "POST":
        project = get_object_or_404(Project, pk=projectid)
        project.total_votes -= 1
        allVotes = Votes.objects.all()
        for vote in allVotes:
            if vote.user == request.user and vote.project == project:
                vote.delete()
        project.save()
        return redirect('detail', projectid=projectid)
