from django.shortcuts import render, redirect
from .models import Task, Place, Reviews, Grade
from .forms import TaskForm
from django.http import HttpResponse
from django.db.models import Avg


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


def login(request):
    return


def register(request):
    return


def grade(request):
    # tasks = Task.objects.order_by('-id')
    # Each restaurant, each with a count of average grade as a "average" attribute.
    average_grade = Grade.objects.values('task').annotate(average=Avg('val')).filter(average__gt=4.3)
    tasks = Task.objects.filter(id__in=average_grade.values('task'))

    context = {
        'title': 'Средние оценки заведений',
        'tasks': tasks,
        'grade': average_grade
    }

    return render(request, 'main/grade.html', context)
