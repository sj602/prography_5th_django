from django import forms
from .models import Article, Comment

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
        exclude = ('article',)
