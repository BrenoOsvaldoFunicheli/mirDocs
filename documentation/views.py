from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, View
from .models import PostBlog
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse


# Create your views here.


class IndexTemplateView(View):
    template_name = "documentation/index.html"

    def get(self, request):
        context = {
            'items': PostBlog.objects.all()
        }

        html = render_to_string('documentation/index.html', context)

        return HttpResponse(html)


class DocumentationTemplateView(View):
    def get(self, request, value):
        print(value)
        context = {
        }
        return render(request, 'documentation/docs-page.html', context)
        # html = render_to_string('documentation/docs-page.html#' + value, context)
        #
        # return HttpResponse(html)