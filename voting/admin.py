from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'active',)
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
