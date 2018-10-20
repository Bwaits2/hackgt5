from django.shortcuts import render

from .forms import FilterForm

# Create your views here.
def homepage(request):
    context = {}
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            context["form"] = form
            return render(request, "main/analysis.html", context)
    else:
        form = FilterForm()
        context["form"] = form
        return render(request, "main/homepage.html", context)


