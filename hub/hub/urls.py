from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings # to import static in deployment
from django.conf.urls.static import static # to import static in deployment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = get_schema_view(
   openapi.Info(
      title="Project Hub API",
      default_version='v1',
      description="Swagger documentation for Project Hub",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
 
    path('admin/', admin.site.urls),
    path('api-auth',include('rest_framework.urls')),
    path('v1/auths/',include('auths.urls'),name='Auths'),
    path('v1/',include('projects.urls'),name='Project')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)