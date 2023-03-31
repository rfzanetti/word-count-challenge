from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from http import HTTPStatus
from waffle import switch_is_active

from counter_app.counter import count_words
from counter_app.hashing import hash_text

WORD_COUNT_CACHE_TIMEOUT = 3600


def index(request):
    return render(request, "index.html")


def counter(request):
    words = request.POST.get("words")

    if not words:
        return JsonResponse({"error_message": "Words are required!"}, status=HTTPStatus.BAD_REQUEST)

    if switch_is_active("WORD_COUNT_CACHE"):
        word_hash = hash_text(words)
        word_count = cache.get(word_hash)

        if not word_count:
            word_count = count_words(words)
            cache.set(word_hash, word_count, timeout=WORD_COUNT_CACHE_TIMEOUT)
    else:
        word_count = count_words(words)

    return JsonResponse({"word_count": word_count})
