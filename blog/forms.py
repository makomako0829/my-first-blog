# from dataclasses import fields
# from msilib.schema import Class
# from pyexpat import model
from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = 'title', 'text',