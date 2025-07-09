import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from openai import OpenAI

openai.api_key = settings.OPENAI_API_KEY


def generate_article(prompt: str) -> str:

    print(f"{prompt=}")
    print(f"{prompt=}")
    print(f"{prompt=}")
    print(f"{prompt=}")
    if not prompt:
        return ""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500,
    )
    print(f"{response=}")
    print(f"{response=}")
    print(f"{response=}")
    print(f"{response=}")
    return response.choices[0].message["content"].strip()
