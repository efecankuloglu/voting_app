from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Question, Choice
from .forms import QuestionForm, ChoiceFormset


def index(request):
    return render(request, 'index.html')


class CreatePoll(View):
    def get(self, request):
        form = QuestionForm()
        formset = ChoiceFormset()
        return render(request, 'create.html', {'form': form,
                                                'formset': formset})

    def post(self, request):
        form = QuestionForm(data=request.POST)
        formset = ChoiceFormset(data=request.POST)
        if form.is_valid() and formset.is_valid():
            question = form.save()
            for forms in formset:
                choice = forms.save(commit=False)
                choice.question = question
                choice.save()
        return redirect('detail', question.pk)


class QuestionListView(ListView):
    template_name = "list.html"
    context_object_name = "question_list"

    def get_queryset(self):
        return Question.actives.order_by('-publish')
        # return Question.objects.filter(publish__gt=timezone.now() - (datetime.timedelta(minutes=1) * F('duration'))).order_by('-publish')


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk, active=True)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(pk,)))


class DetailView(DetailView):
    model = Question
    template_name = "detail.html"
    queryset = Question.actives.all()

class ResultsView(DetailView):
    model = Question
    template_name = 'results.html'
