from django.db import models



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
    name = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.content}: {self.id}'