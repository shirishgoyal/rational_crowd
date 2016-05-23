from rest_framework import viewsets

from rational_crowd.api.serializers.questionnaire import QuestionnaireSerializer
from rational_crowd.questionnaire.models import Questionnaire


class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
