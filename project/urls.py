from django.contrib import admin
from django.urls import path, include
from invista_me import views as invista_me_views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', invista_me_views.investimentos, name='investimentos'),
    path('<int:id_investimento>', invista_me_views.detalhes, name='detalhes'),
    path('novo_investimento/', invista_me_views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', invista_me_views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', invista_me_views.excluir, name='excluir'),
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('', include('usuarios.urls')),
]
