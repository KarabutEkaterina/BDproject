from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task, Place, Reviews, Grade, Services
from .forms import TaskForm, LoginForm
from django.db.models import Avg, F
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    # list of objects
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def admin(request):
    return redirect('admin')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def address(request, item_id):
    place = Place.objects.get(task=item_id)

    return render(request, 'main/address.html', {'title': 'Информация об адресе', 'place': place})


# return HttpResponse(f"страница с адресом номера {item_id}")

def reviews(request, item_id):
    review = Reviews.objects.filter(task=item_id).order_by('-time')

    return render(request, 'main/reviews.html', {'title': 'Отзывы о данном ресторане', 'review': review})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    context = {'form': form,
               'title': 'Вход в систему'
               }

    return render(request, 'main/login.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт был создан для пользователя' + user)
            return redirect('login')

    context = {'form': form,
               'title': 'Регистрация пользователя'
               }

    return render(request, 'main/register.html', context)


def grade(request):
    # tasks = Task.objects.order_by('-id')
    # Each restaurant, each with a count of average grade as a "average" attribute.
    average_grade = Grade.objects.values('task').annotate(average=Avg('val')).filter(average__gt=4.3)
    tasks = Task.objects.filter(id__in=average_grade.values('task'))

    # print(connection.queries)

    context = {
        'title': 'Средние оценки заведений',
        'tasks': tasks,
        'grade': average_grade
    }

    return render(request, 'main/grade.html', context)


def services(request):
    serv = Services.objects.all().select_related('task')

    context = {
        'title': 'Дополнительные услуги',
        'services': serv,
    }

    return render(request, 'main/services.html', context)


def event(request):
    task = Task.objects.values('title').annotate(event_name=F('event__name'), date=F('event__event_date'),
                                                 description=F('event__description'))

    context = {
        'title': 'Ближайшие меропрятия',
        'tasks': task,
    }

    return render(request, 'main/event.html', context)
