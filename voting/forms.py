from django import forms
from django.forms import inlineformset_factory

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'duration',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)


ChoiceFormset = inlineformset_factory(
    Question,
    Choice,
    form = ChoiceForm,
    extra= 3,
    can_delete=False,
)