from django.urls import path

from ..services.openai_client import generate_article
from ..views.article import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)
from ..views.article import ArticleCreateView, ask_ai

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/new/", ArticleCreateView.as_view(), name="article-create"),
    path("articles/<int:pk>/edit/", ArticleUpdateView.as_view(), name="article-update"),
    path(
        "articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article-delete"
    ),
    path("generate_article/", generate_article, name="generate_article"),
]
