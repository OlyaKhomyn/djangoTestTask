from users.serializers import UserSerializer
from users.models import User
from rest_framework import generics


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        registration = self.request.query_params.get('registration', None)
        if registration is not None:
            queryset = queryset.filter(registration=registration)
        return queryset
