from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:article_id>/edit', views.edit, name='edit'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>', views.detail, name='detail'),
    # path('add_comment', views.add_comment, name='add_comment'),
]