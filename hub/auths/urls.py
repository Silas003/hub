from . import views
from rest_framework.routers import DefaultRouter

app_name='Auths'
router=DefaultRouter()

router.register('register',views.RegistrationViewset,basename='register')
router.register('login',views.LoginViewset,basename='login')

urlpatterns=[]
urlpatterns+=router.urls