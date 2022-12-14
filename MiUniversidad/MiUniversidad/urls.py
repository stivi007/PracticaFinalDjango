"""MiUniversidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
 #username=esteban
 #password=admin123


from Academica.views import CarreraViewSet,EstudianteViewSet,CursoViewSet,MatriculaViewSet,carrera_contador
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path,include


router=DefaultRouter()
router.register(r"carrera",CarreraViewSet)
router.register(r"estudiante",EstudianteViewSet)
router.register(r"curso",CursoViewSet)
router.register(r"matricula",MatriculaViewSet)

urlpatterns = [
   
    path('admin/', admin.site.urls),
    
    path('',include(router.urls)),
    path('carrera/cantidad',carrera_contador)
]
