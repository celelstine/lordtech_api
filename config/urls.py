"""lordtechApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.schemas import get_schema_view

from rest_framework.renderers import CoreJSONRenderer, JSONOpenAPIRenderer

schema_view = get_schema_view(title='Lordtech Sales API',
                              description='API to manages sales at lordtech',
                              url='http://localhost:8000/',
                              version='1.0.0',
                              renderer_classes=[
                                  CoreJSONRenderer, JSONOpenAPIRenderer],
                              authentication_classes=[],
                              permission_classes=[])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view, name="docs"),
    path('api/', include(('api.urls', 'api'), namespace='api')),
]
