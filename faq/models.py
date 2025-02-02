from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Translate question and answer into Hindi and Bengali
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_text(self, field, lang):
        # Method to retrieve translated text dynamically
        translated_field = f"{field}_{lang}"
        return getattr(self, translated_field, getattr(self, field))

    def __str__(self):
        return self.question

def save(self, *args, **kwargs):
    translator = Translator()
    print("Translating question to Hindi...")
    self.question_hi = translator.translate(self.question, dest='hi').text
    print(f"Translated question (Hindi): {self.question_hi}")
    print("Translating question to Bengali...")
    self.question_bn = translator.translate(self.question, dest='bn').text
    print(f"Translated question (Bengali): {self.question_bn}")
    print("Translating answer to Hindi...")
    self.answer_hi = translator.translate(self.answer, dest='hi').text
    print(f"Translated answer (Hindi): {self.answer_hi}")
    print("Translating answer to Bengali...")
    self.answer_bn = translator.translate(self.answer, dest='bn').text
    print(f"Translated answer (Bengali): {self.answer_bn}")
    super().save(*args, **kwargs)