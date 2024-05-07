from rest_framework import viewsets,status
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .models import Project
from utils.functions import generate_project_id
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def create(self, request:Request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['id']=generate_project_id()
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        