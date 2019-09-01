from django import forms
from .models import Article, Comment

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')

class CommentPostForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     article_id = kwargs.pop('article_id', None)
    #     super(CommentPostForm, self).__init__(*args, **kwargs)
    #
    #     if article_id:
    #         self.fields['article_id'].queryset = Article.objects.filter(pk=article_id)

    class Meta:
        model = Comment
        fields = ('author', 'content', 'article')
