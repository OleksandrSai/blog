import json
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from openai import OpenAI

from TechProject import settings
from ..models.article import Article, ArticleImage
from ..forms.article import ArticleForm
from ..services.openai_client import generate_article


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    paginate_by = 3
    context_object_name = "object_list"
    ordering = ["-created_at"]


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/article_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Генерировать тело статьи, только если оно пустое (и есть prompt)
        if not form.cleaned_data.get("body") and form.cleaned_data.get("prompt"):
            form.instance.body = generate_article(form.cleaned_data.get("prompt"))

        response = super().form_valid(form)

        for file in self.request.FILES.getlist("images"):
            ArticleImage.objects.create(article=self.object, image=file)

        return response


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/article_form.html"
    success_url = reverse_lazy("article-list")

    def test_func(self):
        return self.get_object().author == self.request.user


client = OpenAI(api_key=settings.OPENAI_API_KEY)


@require_POST
@csrf_exempt
def ask_ai(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Некоректний JSON"}, status=400)

    prompt = data.get("prompt")
    print(f"prompt={prompt}")
    if not prompt:
        return JsonResponse({"error": "Запит порожній"}, status=400)

    full_prompt = f"Напиши статтю на тему: {prompt}\n\nЗаголовок і текст статті:"

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Ти — помічник, який пише статті."},
                {"role": "user", "content": full_prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )

        text = response.choices[0].message.content.strip()
        lines = text.split("\n", 1)
        title = lines[0] if len(lines) > 0 else ""
        body = lines[1] if len(lines) > 1 else text

        return JsonResponse({"title": title, "body": body})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("article-list")

    def test_func(self):
        return self.get_object().author == self.request.user
