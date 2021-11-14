from django.shortcuts import render
from .search import Searcher


def index(request):
    return render(request, 'main/index.html')


def result(request):
    if request.method == "POST":
        age = request.POST.get("age")
        money = request.POST.get("money")
        family = request.POST.get("family")
        location = request.POST.get("location")
        fastcar = request.POST.get("fastcar")
        searcher = Searcher(age, money, family, location, fastcar)
        results = searcher.get_result()
        return render(request, 'main/result.html', {'results': results})