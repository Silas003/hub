from django.db import models
from auths.models import User

class Project(models.Model):
    class ProjectType(models.TextChoices):
        FINAL='Final'
        MINI='Mini'
    title=models.CharField(max_length=255)
    student=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    documentation=models.TextField(max_length=1000000)
    file=models.FileField(upload_to=f'projects/{student}',null=True,blank=True)
    supervised_by=models.CharField(max_length=500)
    project_type=models.CharField(choices=ProjectType.choices,default='Mini',max_length=10)
    year=models.DateField(auto_now_add=True)
    date_created=models.DateField(auto_now_add=True)
    last_updated=models.DateField(auto_now=True)
    link=models.URLField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering=('-year',)