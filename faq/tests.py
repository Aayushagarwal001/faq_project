import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_model():
    # Create an FAQ entry
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )

    # Test the model's __str__ method
    assert str(faq) == "What is Django?"

    # Test the get_translated_text method
    assert faq.get_translated_text('question', 'en') == "What is Django?"
    assert faq.get_translated_text('answer', 'en') == "Django is a web framework."

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()

    # Create an FAQ entry
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )

    # Test the API without language parameter (default to English)
    url = reverse('faq-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"
    assert response.data[0]['answer'] == "Django is a web framework."

    # Test the API with Hindi language parameter
    response = client.get(url, {'lang': 'hi'})
    assert response.status_code == 200
    assert response.data[0]['question'] != "What is Django?"  # Should be translated
    assert response.data[0]['answer'] != "Django is a web framework."  # Should be translated