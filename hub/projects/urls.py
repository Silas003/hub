from . import views
from rest_framework.routers import DefaultRouter

app_name='Project'
router=DefaultRouter()

router.register('project',views.ProjectViewset,basename='project')

urlpatterns=[]
urlpatterns+=router.urls