from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

'''
for viewing actual sql query

python manage.py sqlmigrate blog 0001
'''

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)  # for updating time and also handling new created post time
    author = models.ForeignKey(User,on_delete=models.CASCADE) # User-Post is one to Many relation, and user is being handled by django auth panel , hence we dont need to craete a seperate user table.

    def __str__(self) -> str:
        return self.title
