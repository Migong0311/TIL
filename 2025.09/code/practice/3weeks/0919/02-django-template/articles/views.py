import random
from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    context = {
        'name': '미성',
        'test': {
            'hobby': 'baseball'
        },
        'nums': [i for i in range(1,11)],
        'names': [f'테스트{i}' for i in range(1, 11)]
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


def detail(request,num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)

def greeting(request,name):
    
    context = {
        'name' : name,
    }
    return render(request, 'articles/greeting.html', context)
