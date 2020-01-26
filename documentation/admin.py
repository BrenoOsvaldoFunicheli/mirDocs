from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(KeyWord)
class KeywordAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']


@admin.register(TypeOfComponent)
class TypeOfComponentAdmin(admin.ModelAdmin):
    pass
