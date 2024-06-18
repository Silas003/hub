from rest_framework import viewsets,status,filters
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .models import Project
from utils.functions import generate_project_id
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['year', 'project_type']
    search_fields = ['title', 'student']
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def create(self, request:Request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['id']=generate_project_id()
        serializer.save()
        
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
            
