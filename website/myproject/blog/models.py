from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Blog(models.Model):
    # Class variables
    title = models.CharField(max_length=50)
    entry = models.TextField()
    date_published = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=30)
    comments = models.TextField()
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.name



class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['name', 'comments', 'email']
        # exclude = ['email']



