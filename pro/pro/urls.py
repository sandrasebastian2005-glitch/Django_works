"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from app import views

# url to veiw mapping
urlpatterns = [
    path('admin/', admin.site.urls),

    #path('routelabel',viewname,'urlname')  # http://127.0.0.1:8000/routelabel , if we give this name then the path should have it else it becomes error

    path('',views.Home),    # http://127.0.0.1:8000/
    path('Index',views.Index),

    # here it shows error bcs this file and function is in app folder 
    # hence we import them from that package

]
