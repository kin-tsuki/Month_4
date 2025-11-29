from django.shortcuts import render, redirect 

from posts.models import Post




def home_page_view(request):
    return render(request, "base.html")
    
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return redirect("/posts/")
    return render(request, "posts/post_detail.html", context={"post": post})
