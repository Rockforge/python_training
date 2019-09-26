from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from .models import Blog, Comment, CommentModelForm
from .forms import CommentForm
from .utils import handleCSV
from .serializers import BlogSerializer

# Class based views
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


#Function based views
def index(request):
    # Get all the posts
    posts = Blog.objects.all()
    context = { 'posts': posts }
    return render(request, 'blog/index.html', context)

def get_post(request, post_id):
    post = Blog.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/post.html', context)

def get_comment_from_user2(request):
    form = CommentModelForm(request.POST)

def get_comment_from_user(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            handleCSV(request.FILES['upload'])
            return HttpResponse('Thank you')
    elif request.method == 'GET':
        form = CommentForm()
    context = {'form': form}
    return render(request, 'blog/comments.html', context)



def get_profile(request):
    # Ask question about middlewares
    if not request.user.is_authenticated:
        # return HttpResponse('Hello World')
        raise Http404('Anonymous not allowed') # Raise this error 

    template = """<b>Name</b>: {}
    <b>Username</b>: {}
    <b>Is Admin</b>: {}
    """.replace('\n', '<br>')

    output = template.format(
        request.user.get_full_name(),
        request.user.get_username(),
        request.user.is_superuser,
    )

    return HttpResponse(output)

