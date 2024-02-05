from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=256)

class Post(models.Model):
    title = models.CharField(max_length=256)
    blog = models.ForeignKey(Blog, null=True, on_delete=models.deletion.SET_NULL)
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField()
