from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import strip_tags
from bs4 import BeautifulSoup


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_first_image_url(self):
        """
        Парсим body и возвращаем URL первой картинки, если есть.
        """
        soup = BeautifulSoup(self.body, "html.parser")
        img = soup.find("img")
        if img and img.has_attr("src"):
            return img["src"]
        return None

    def get_short_text(self, words=25):
        """
        Возвращает короткий текст без тегов, обрезанный до N слов.
        """
        text = strip_tags(self.body)
        return " ".join(text.split()[:words]) + (
            "..." if len(text.split()) > words else ""
        )

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(
        Article, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="articles/images/")
