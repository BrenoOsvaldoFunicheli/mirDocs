from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(PostBlog)
class PostBlogAdim(admin.ModelAdmin):
    pass


@admin.register(TypeComponent)
class ComponentAdim(admin.ModelAdmin):
    pass
