from django.shortcuts import render
from .recommend import Recommender
from .rule import Rule


def index(request):
    return render(request, 'main/index.html')


def result(request):
    if request.method == "POST":
        age = request.POST.get("age")
        money = request.POST.get("money")
        family = request.POST.get("family")
        location = request.POST.get("location")
        fastcar = request.POST.get("fastcar")
        recommender = Recommender(age, money, family, location, fastcar)
        results = recommender.get_result()
        return render(request, 'main/result.html', {'results': results})


def admin(request):
    return render(request, 'main/admin.html')


def admin_search(request):
    if request.method == "POST":
        query = request.POST.get("text")
        rule = Rule(query)
        results = rule.get_result()
        return render(request, 'main/search.html', {'results': results, 'query': query})
    elif request.method == "GET":
        return render(request, 'main/search.html')


def admin_add(request):
    if request.method == "POST":
        query = request.POST.get("query")
        print("!"*100)
        print(query)
        rule = Rule(query)
        rule.add_rule()
        return render(request, 'main/add.html')
    elif request.method == "GET":
        return render(request, 'main/add.html')
