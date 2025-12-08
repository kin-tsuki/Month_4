from django.db import models



"""
insert into post title, content VALUES(title1, content1) ==> Post.objects.create(title="title1", content="content1")
"""



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class Tag(models.Model):
    name = models.CharField(max_length=156)

    def __str__(self):
        return f"{self.name}"

                            

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.content}: {self.id}'

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')

    def __str__(self):
        return f'{self.post.title}'