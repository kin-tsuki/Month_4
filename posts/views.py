from django.shortcuts import render, redirect 
from django.http import HttpResponse

from posts.models import Post
from posts.forms import PostCreateForm, PostForm2, CommentForm


def home_page_view(request):
    return render(request, "base.html")
    
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return redirect("/posts/")
   

    if request.method == "GET":
        form = CommentForm()
        return render(request, "posts/post_detail.html", context={"post": post, "form": form})
    

    return render(request, "posts/post_detail.html", context={"post": post})

def post_create_view(request):
    if request.method == "GET":
        form = PostCreateForm() # PostForm2
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method =="POST":
        form = PostCreateForm(request.POST, request.FILES)     # PostForm2
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            post = Post.objects.create(title=title, content=content, image=image)
            # form.save()
        else:
            return render(request, "posts/post_create.html", context={"form": form})
        return redirect("/posts/")
    

    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # image = request.FILES.get("image")


  