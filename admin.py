from django.contrib import admin
from myapp.models import Lesson, Product, Owner, User


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'url', 'duration',]
    list_filter = ['title', 'duration',]


@admin.register(Product)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'lesson',]
    list_filter = ['title', 'lesson',]


@admin.register(Owner)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'product',]
    list_filter = ['first_name', 'last_name', 'product',]


@admin.register(User)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',]
    list_filter = ['first_name', 'last_name',]