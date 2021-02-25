from django.urls import path, include
from .views import AdminView

urlpatterns = [
    path('', AdminView.as_view())
]
