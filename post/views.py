from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from post.forms import PostForm
from post.models import Post


def index(request):
    form = PostForm()
    posts = Post.objects.all()
    return render(
        request, 'index.html',
        context={'posts': posts, 'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(text=form.cleaned_data['text'])
            return HttpResponseRedirect('/')


def hello(request):
    posts = Post.objects.all()
    return render(request, "threads.html",
                  context={'posts': posts})