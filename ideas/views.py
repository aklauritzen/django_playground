from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ideas.models import Idea

from .forms import IdeaModelForm


# Create your views here.
def ideas_view(request, *args, **kwargs):
    qs = Idea.objects.all()
    context = {"object_list": qs}    
    return render(request, "ideas.html", context)

# @staff_member_required
def idea_create_view(request, *args, **kwargs):
    form = IdeaModelForm(request.POST or None)    
    
    # FIXME: Why is this not valid?
    if form.is_valid():
        print("Form is VALID")
        obj = form.save(commit=False)
        obj.save()
        form = IdeaModelForm()

    return render(request, "create_idea.html", {"form": form})
