from django.urls import path
from .views import list_todos, create_todos, delete_todo, update_todos

urlpatterns = [
    path('', list_todos),
    path('create/', create_todos),
    path('delete/<int:pk>/', delete_todo),
    path('update/<int:primary_key>/', update_todos)
]