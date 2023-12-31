"""
URL configuration for mysite project.

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
from django.urls import path

from personal.views import (
    home_screen_view,
    about_screen_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
)

from todotask.views import (
    todo_screen_view,
    delete,
    change_status_na,
    change_status_wip,
    change_status_done,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('about/', about_screen_view, name='about'),
    path('todo/', todo_screen_view, name='todo'),
    path('delete/<id>', delete, name='delete'),
    path('change_status_na/<id>', change_status_na, name='change_status_na'),
    path('change_status_wip/<id>', change_status_wip, name='change_status_wip'),
    path('change_status_done/<id>', change_status_done, name='change_status_done'),
]
