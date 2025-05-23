from django.urls import re_path

from apps.recommendations.views import RecommendFromSpeechView

app_name = "recommendations"
urlpatterns = [
    re_path(r"from-speech/(?P<filename>[^/]+)$", RecommendFromSpeechView.as_view())
]
