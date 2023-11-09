from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def SDGs(request):
    goals = Goal.objects.all()
    return render(request, 'goals.html', {'goals': goals})

@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'goal_detail.html', {'goal': goal})
