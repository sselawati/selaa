"""untirta URL Configuration

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
from django.contrib import admin
from django.urls import path
from faperta.views import Faperta
from feb.views import Feb
from fh.views import Fh
from fisip.views import Fisip
from fk.views import Fk
from fkip.views import Fkip
from ft.views import Ft
from pascasarjana.views import Pascasarjana

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', Faperta),
    path('feb/', Feb),
    path('fh/', Fh),
    path('fisip/', Fisip),
    path('fk/', Fk),
    path('fkip/', Fkip),
    path('ft/', Ft),
    path('pascasarjana/', Pascasarjana),

]
