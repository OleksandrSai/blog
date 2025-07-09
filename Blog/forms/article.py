from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from ..models.article import Article
from .widgets import MultiFileInput


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    prompt = forms.CharField(
        label="Запит до ШІ",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Article
        fields = ["title", "body", "prompt"]  # добавляем prompt сюда
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
        }
