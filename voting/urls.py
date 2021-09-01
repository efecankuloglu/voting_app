from django.urls import path

from .views import index, CreatePoll, QuestionListView, DetailView, vote, ResultsView

urlpatterns = [
    path('', index, name='index'),
    path('create/', CreatePoll.as_view(), name='create'),
    path('list/', QuestionListView.as_view(), name='all_questions'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/vote/', vote, name='vote'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
]
