from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=[
            'title',
            'documentation',
            'supervised_by',
            'project_type',
            'student',
            'file'
            'link',
            'year'
        ]

        read_only_fields =[
            'id',
            'year',
            'last_updated',
        ]