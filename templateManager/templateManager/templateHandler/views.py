from django.views.generic import TemplateView
from .models import NavbarOption, Post, Image, About, HomeDesign
from django.http import JsonResponse
import json


class WorkView(TemplateView):
    template_name = 'work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["navOptions"] =  NavbarOption.objects.all()
        
        try:
            NavbarOptionName = NavbarOption.objects.get(name = self.kwargs['slug2'])
            posts = Post.objects.filter(menu = NavbarOptionName).order_by('-updated')
            extra_images = Image.objects.filter(post__menu = NavbarOptionName)                       
            context['posts'] = posts
            context['extra_photos'] = extra_images
            context['NavbarName'] = NavbarOptionName
            dumpData = homeInfo()
            context['serialized_data'] = dumpData
            
        except:
            default_menu = NavbarOption.objects.get(name = 'Service')
            posts = Post.objects.filter(menu = default_menu).order_by('-updated')
            extra_images = Image.objects.filter(post__menu = default_menu)                       
            context['posts'] = posts
            context['extra_photos'] = extra_images
            context['NavbarName'] = 'Service'
            dumpData = homeInfo()
            context['serialized_data'] = dumpData

        return context
    

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dumpData = homeInfo()
        context['NavbarName'] = 'Home'
        context['serialized_data'] = dumpData
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["aboutArticels"] =  About.objects.all()
        context['NavbarName'] = 'About'
        dumpData = homeInfo()
        context['serialized_data'] = dumpData
        return context

def homeInfo():
    second = list(HomeDesign.objects.all().values())
    try:
        dict = second[0]
    except:
        dict = {}
    return json.dumps(dict)