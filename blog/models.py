from django.db import models
from django.contrib.auth.models import User
import os

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE) # author db 삭제시 작성한 글도 삭제
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # author db 삭제시 작성자명을 빈칸으로 둔다

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}' # {self.pk}: 포스트의 pk 값, self.title}: 포스트의 title 값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]