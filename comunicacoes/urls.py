from django.urls import path

from comunicacoes.views import create_comunicacao, delete_comunicacao, list_comunicacoes, update_comunicacao

urlpatterns = [
    path('', list_comunicacoes, name='list_comunicacoes'),
    path('new', create_comunicacao, name='create_comunicacao'),
    path('update/<int:id>/', update_comunicacao, name='update_comunicacao'),
    path('delete/<int:id>/', delete_comunicacao, name='delete_comunicacao'),
]