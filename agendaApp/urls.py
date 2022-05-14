"""agendaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendaApp/', views.lista_eventos),
    path('agendaApp/lista/<int:id_usuario>', views.json_lista_evento),
    path('agendaApp/evento/', views.evento),
    path('agendaApp/evento/submit', views.submit_evento),
    path('agendaApp/evento/delete/<int:id_evento>/', views.delete_evento),
    path('', RedirectView.as_view(url='/agendaApp/')), # path('', views.index) #redireciona a page inicial para o index
    path('login/', views.login_user), #função de login
    path('login/submit', views.submit_login), #submeter login
    path('logout/', views.logout_user) #função de logout

]
