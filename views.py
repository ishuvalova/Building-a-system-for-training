from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Lesson, Product, Owner, User
import random


def create_lesson(request):

    lesson = Lesson(
        title=random.choice(['lesson1', 'lesson2', 'lesson3']),
        content='content',
        url='url',
        duration='duration',
    )
    lesson.save()

    return HttpResponse({lesson.title}, {lesson.content}, {lesson.url}, {lesson.duration})


def create_product(request):
    product = Product(
        title="title",
        lesson='lesson',
    )
    product.save()

    return HttpResponse({product.title}, {product.lesson})


def create_owner(request):
    owner = Owner(
        first_name='first_name',
        last_name='last_name',
    )
    owner.save()

    return HttpResponse({owner.first_name}, {owner.last_name})


def create_user(request):
    user = User(
        first_name='first_name',
        last_name='last_name',
    )
    user.save()

    return HttpResponse({user.first_name, user.last_name})


def list_lessons(request):   # вывод списка всех уроков
    lesson_object = Lesson.objects.all()
    lessons = [f'{lesson.title}, {lesson.duration}' for lesson in lesson_object]
    return HttpResponse('<br>'.join(lessons))


def list_products(request):    # вывод списка продуктов
    product_object = Product.objects.all()
    products = [f'{product.title}' for product in product_object]
    return HttpResponse('<br>'.join(products))






