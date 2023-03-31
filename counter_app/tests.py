from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus
from waffle.testutils import override_switch

from counter_app.counter import count_words
from counter_app.hashing import hash_text


class TestCounterEndpoint(TestCase):
    def test_submitting_empty_words_returns_bad_request(self):
        response = self.client.post(
            reverse("counter"), data={"words": ""}
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {"error_message": "Words are required!"}

    def test_submit_returns_success(self):
        response = self.client.post(
            reverse("counter"), data={"words": "this is a test"}
        )
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"word_count": 4}

    def test_cache_was_correctly_set(self):

        words = "this is a test"
        words_hash = hash_text(words)

        with override_switch("WORD_COUNT_CACHE", active=True):
            assert not cache.get(words_hash)

            self.client.post(
                reverse("counter"), data={"words": words}
            )

            assert cache.get(words_hash) == 4

    def test_cache_was_correctly_used(self):

        words = "this is a test"
        words_hash = hash_text(words)

        with override_switch("WORD_COUNT_CACHE", active=True):
            cache.set(words_hash, 999, timeout=3600)

            response = self.client.post(
                reverse("counter"), data={"words": words}
            )

            assert response.json() == {"word_count": 999}


class TestCounter(TestCase):

    def test_empty_words(self):
        words = ""
        assert count_words(words) == 0

    def test_all_spaces(self):
        words = "             "
        assert count_words(words) == 0

    def test_single_word(self):
        words = "test"
        assert count_words(words) == 1

    def test_multiple_spaces(self):
        words = "multiple     spaces"
        assert count_words(words) == 2

    def test_leading_and_trailing_spaces(self):
        words = " does it ignore leading and trailing spaces "
        assert count_words(words) == 7

    def test_other_kinds_of_delimiters(self):
        words = "lets check (other kinds of) delimiters...should work!"
        assert count_words(words) == 8

    def test_hyphens_and_apostrophes(self):
        words = "let's see what the know-how of our method with hyphens and apostrophes"
        assert count_words(words) == 12


class TestHashing(TestCase):
    def test_hash_text(self):
        assert hash_text(
            "this is a test") == "2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c"
