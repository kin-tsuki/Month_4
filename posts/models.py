from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.content}: {self.id}'