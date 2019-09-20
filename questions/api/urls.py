from django.urls import include, path
from rest_framework.routers import DefaultRouter
from questions.api import views as view

router = DefaultRouter()
router.register(r"questions", view.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("questions/<slug:slug>/answers/", view.AnswerListAPIView.as_view(), name="answer-list"),
    path("questions/<slug:slug>/answer/", view.AnswerCreateAPIView.as_view(), name="answer-create"),
    path("answers/<int:pk>/", view.AnswerRUDAPIView.as_view(), name="answer-detail"),
    path("answers/<int:pk>/like/", view.AnswerLikeAPIView.as_view(), name="answer-like")
]