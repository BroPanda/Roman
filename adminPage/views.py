from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from .serializers import ConstrProjSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication

UserModel = get_user_model()


class AdminView(CreateAPIView, ListModelMixin):
    serializer_class = ConstrProjSerializer
    # queryset = ConstrProjModel.objects.all() # переопреділено в get_queryset
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        id = params.get('id', None)
        if not id:
            return UserModel.objects.all()
        return UserModel.objects.filter(id=id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
