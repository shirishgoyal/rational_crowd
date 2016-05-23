from rest_framework import serializers

from rational_crowd.api.serializers.utils import DynamicFieldsModelSerializer
from rational_crowd.questionnaire.models import Questionnaire, Question, QuestionOption


class QuestionnaireSerializer(DynamicFieldsModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Questionnaire
        fields = ('name', 'questions')

    def get_questions(self, obj):
        serializer = QuestionSerializer(obj.questions, many=True)
        return serializer.data


class QuestionSerializer(DynamicFieldsModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'content', 'is_multiple_choice', 'options')

    def get_options(self, obj):
        serializer = QuestionOptionSerializer(obj.options, many=True)
        return serializer.data


class QuestionOptionSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = QuestionOption
        fields = ('id', 'content')
