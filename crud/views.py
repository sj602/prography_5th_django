from django.shortcuts import render, redirect
from django.db.models import F
from .models import Article, Comment
from .forms import ArticlePostForm, CommentPostForm


def index(request):
    print("home!!!")
    all_articles = Article.objects.all()

    if len(all_articles) == 0:
        all_articles = {
            'all_articles': None
        }
        return render(request, 'index.html', all_articles)

    all_articles = {
        'all_articles': all_articles
    }

    return render(request, 'index.html', all_articles)


def add(request):
    if request.method == 'POST':
        form = ArticlePostForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('index')
    else:
        form = ArticlePostForm()

    return render(request, 'add.html', {'form': form})


def detail(request, article_id):
    def _add_comment():
        form = CommentPostForm(request.POST)
        print("comment form :", form)
        if form.is_valid():
            print("in valid")
            form.save()
            print("saved")

    if request.method == 'GET':
        article = Article.objects.get(pk=article_id)
        article.hits = F('hits') + 1
        article.save()
        form = CommentPostForm()
        comments = article.article_comments.all()
        ctx = {
            'article': article,
            'comments': comments,
            'form': form
        }
    elif request.method == 'POST':
        print("article_id:", article_id)
        _add_comment()
        article = Article.objects.get(pk=article_id)
        print("article:", article)
        comments = article.article_comments.all()
        print("comments:", comments)
        form = CommentPostForm()
        ctx = {
            'article': article,
            'comments': comments,
            'form': form
        }

    return render(request, 'detail.html', ctx)

0
def edit(request, article_id):
    print("--------132413451345")
    article = Article.objects.get(pk=article_id)
    ctx = {
        'article': article
    }
    print("article:", article)

    if request.method == 'POST':
        print(1)
        form = ArticlePostForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            print("article updated", article)
            return redirect('detail', article_id=article_id)
    else:
        print(2)
        form = ArticlePostForm(instance=article)
        print("formmmmmmm:", form)
        ctx['form'] = form

    return render(request, 'edit.html', ctx)


def delete(request, article_id):
    article = Article.objects.filter(pk=article_id)
    article.delete()

    return redirect('index')