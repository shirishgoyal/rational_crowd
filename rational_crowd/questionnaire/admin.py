from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib import admin

from .models import Questionnaire, Question, QuestionOption


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = (QuestionInline,)

admin.site.register(Questionnaire, QuestionnaireAdmin)


class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('questionnaire', 'content', 'is_multiple_choice')
    inlines = (QuestionOptionInline,)

admin.site.register(Question, QuestionAdmin)


# class QuestionOptionAdmin(admin.ModelAdmin):
#     list_display = ('question', 'content', 'is_correct')
#
# admin.site.register(QuestionOption, QuestionOptionAdmin)
