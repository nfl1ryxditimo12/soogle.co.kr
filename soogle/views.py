from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    pass

class PostView(FormView):
    template_name = 'post/post.html'
    form_class = PostForm
    success_url = 'post/'
