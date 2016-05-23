from django.utils.translation import ugettext_lazy as _
from django.db import models
from model_utils.models import TimeStampedModel


class Questionnaire(TimeStampedModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        verbose_name = "Questionnaire"
        verbose_name_plural = "Questionnaires"
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Question(TimeStampedModel):
    questionnaire = models.ForeignKey(Questionnaire, related_name='questions')
    content = models.TextField(verbose_name=_('Content'))
    is_multiple_choice = models.BooleanField(verbose_name=_('Is Multiple Choice?'), default=False)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ('-created',)

    def __str__(self):
        return self.content


class QuestionOption(TimeStampedModel):
    question = models.ForeignKey(Question, related_name='options')
    content = models.TextField(verbose_name=_('Content'))
    is_correct = models.BooleanField(verbose_name=_('Is correct?'), default=False)

    class Meta:
        verbose_name = "Question Option"
        verbose_name_plural = "Question Options"
        ordering = ('-created',)

    def __str__(self):
        return self.content


class QuestionnaireSubmission(TimeStampedModel):
    questionnaire = models.ForeignKey(Questionnaire, related_name='submissions')
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'), blank=True, null=True)

    class Meta:
        verbose_name = "Questionnaire Submission"
        verbose_name_plural = "Questionnaire Submissions"
        ordering = ('-created',)

    def __str__(self):
        return self.ip_address


class QuestionResponse(TimeStampedModel):
    questionnaire_submission = models.ForeignKey(QuestionnaireSubmission, related_name='question_responses')
    question = models.ForeignKey(Question, related_name='responses')
    response = models.ForeignKey(QuestionOption, related_name='+')

    class Meta:
        verbose_name = "Questionnaire Response"
        verbose_name_plural = "Questionnaire Responses"
        ordering = ('-created',)

    def __str__(self):
        return self.response.content
