from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Teacher, Course, Student


# Create your views here.
def index(request):
    teachers = Teacher.objects.all()

    return render(request, 'course.html', {'teachers': teachers})


def create(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '')
        introduce = request.POST.get('introduce', '')
        fans = request.POST.get('fans', 0)
        teacher = Teacher()
        teacher.nickname = nickname
        teacher.introduction = introduce
        teacher.fans = int(fans)
        teacher.save()
        return redirect('/courses/index')

    return render(request, 'add.html')


def update(request, name):
    if request.method == 'GET':
        teacher = Teacher.objects.filter(nickname=name)

        return render(request, 'update.html', {'teacher': teacher[0]})
    if request.method == 'POST':
        introduce = request.POST.get('introduce', '')
        fans = request.POST.get('fans', 0)
        Teacher.objects.filter(nickname=name).update(
            introduction=introduce,
            fans=fans
        )
        return redirect(reverse('courses:index'))


def delete(request, name):
    Teacher.objects.get(nickname=name).delete()
    return redirect(reverse('courses:index'))
