"""
URL configuration for tutorial01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
=======
from django.urls import path

urlpatterns = [
>>>>>>> 5562b15 (Revert "Revert "First commit after Django APP Creation"")
=======
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
>>>>>>> 2ab3ac551ecde50528c8be5c880dd0dfe87e675b
    path('admin/', admin.site.urls),
]
