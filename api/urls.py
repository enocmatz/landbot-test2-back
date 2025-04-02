from django.urls import path 

from api.views.assistance import AssistanceView
from api.views.health import health_check

urlpatterns = [
    path('assistance/', AssistanceView.as_view(), name='assistance'),
    path('health/', health_check, name='health'),
]