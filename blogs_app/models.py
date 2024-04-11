from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    # Foreign Keys
    author:int = models.ForeignKey(User, on_delete=models.CASCADE,related_name="author_username")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=500)
    published_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    # Foreign Keys
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user_id} || {self.post_id} || {self.comment}"
