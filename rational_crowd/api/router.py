from rest_framework import routers

from rational_crowd.api.viewsets.questionnaire import QuestionnaireViewSet

router = routers.DefaultRouter()
router.register(r'questionnaire', QuestionnaireViewSet)
