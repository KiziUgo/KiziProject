from django import forms
from .models import CommentCarPosts, CommentTechPosts, PostCars



class CommentFormCars(forms.ModelForm):
    class Meta:
        model = CommentCarPosts
        fields = ('name','content')

        widgets = {
              'name': forms.TextInput(attrs={'class': 'form-control'}),
              'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentFormTech(forms.ModelForm):
    class Meta:
        model = CommentTechPosts
        fields = ('name','content')

        widgets = {
              'name': forms.TextInput(attrs={'class': 'form-control'}),
              'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

