from django.urls import path
from .views import PracticingView

urlpatterns = [
    path ('practice/', PracticingView.as_view(), name='practice'),
]
