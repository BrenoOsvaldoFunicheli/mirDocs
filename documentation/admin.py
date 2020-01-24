from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(KeyWord)
class KeywordAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeOfComponent)
class TypeOfComponentAdmin(admin.ModelAdmin):
    pass
