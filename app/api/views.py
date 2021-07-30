from app.models import blog
from app.api.serializers import blogSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class blogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = blogSerializer
    authentication_classes = [SessionAuthentication]
    permissions_classes = [IsAuthenticatedOrReadOnly]