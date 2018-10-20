from django.shortcuts import render

from .forms import FilterForm
from .api import callAPI

# Create your views here.
def homepage(request):
    context = {}
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():

            words = ""

            # call api here based on form
            if request.POST.get('include_neutral') == 'on':
               words += callAPI('neutral')
            if request.POST.get('include_democrat') == 'on':
               words += callAPI('democrat')
            if request.POST.get('include_republican') == 'on':
               words += callAPI('republican')

            words = words.split(" ")

            index = 0
            for x in words:
                for y in x:
                    if not y.isalpha():
                        del words[index]
                if len(x) < 3:
                    del words[index]
                index += 1

            context["form"] = form
            context["words"] = words
            return render(request, "main/analysis.html", context)
    else:
        form = FilterForm()
        context["form"] = form
        return render(request, "main/homepage.html", context)


