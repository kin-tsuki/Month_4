from django.shortcuts import render, redirect 
from django.http import HttpResponse

from posts.models import Post, Comment
from posts.forms import PostCreateForm, PostForm2, CommentForm
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    if request.method == "GET":
        return render(request, "base.html")
    
@login_required(login_url="/login/")
def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"posts": posts})

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return redirect("/posts/")
    
    comments = Comment.objects.filter(post=post)

    if request.method == "GET":
        form = CommentForm()
        return render(request, "posts/post_detail.html", context={"post": post, "form": form, "comments": comments})

    if request.method == "POST":
        post = Post.objects.filter(id=post_id).first()
        form = CommentForm(request.POST)
        if not form.is_valid():
             return render(request, "posts/post_detail.html", context={"post": post, "form": form, "comments": comments})
        text = form.cleaned_data.get("text")
        Comment.objects.create(post = post, text=text)
        return redirect(f"/posts/{post_id}")

    

@login_required(login_url="/login/")
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


  