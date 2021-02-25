from django.urls import path, include
from .views import ConstrProjView

urlpatterns = [
    path('', ConstrProjView.as_view())
]
