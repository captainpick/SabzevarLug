from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Post,News,Images_Info,Images
# Create your views here.
from django.core import serializers
from .models import Post
from django import template
import datetime
from os.path import splitext

def Home (request):
    post = Post.objects.filter(Status='p')
    paginator = Paginator(post,5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
  
    
    page_obj = paginator.get_page(page_number)
    number = paginator.num_pages
    

    return render(request,"app_html/home.html",{'post':page_obj,'number':number})


def PostPage(request,slug):
    PostBlog = Post.objects.all().filter(Slug = slug)

   
    
    return render(request , "app_html/blog-single-without-sidebar.html",{'Postblog':PostBlog})



# register = template.Library()


# @register.filter
# def noext(value):
#     return splitext(value)[0]

def Calendar(request):
    return HttpResponse('ok')


def News_Home(request):
    news = News.objects.filter(Status='p')
    paginator = Paginator(news,5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
  
    
    page_obj = paginator.get_page(page_number)
    number = paginator.num_pages
    

    return render(request,"app_html/news.html",{'news':page_obj,'number':number})

def News_Post(request,slug):
    news = News.objects.all().filter(Slug = slug,Status='p')


    return render(request,"app_html/news_post.html",{'news':news})


def Meet_Image(request):
    image=Images_Info.objects.all()
    paginator = Paginator(image,5)
    page_obj = paginator.get_page(1)

    return render(request,"app_html/meet_image.html",{'images':page_obj})




def Meet_Image_Desc(request,slug):
    selected_post=Images_Info.objects.all().filter(Slug=slug)
    other_image = Images.objects.filter(image_rel__in=selected_post)
    
    

    return render(request,"app_html/meet_image_desc.html",{'images':selected_post,'other_image':other_image})