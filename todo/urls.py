from django.urls import path

from todo.views import TodoModelView,TodoModelDetailView

app_name = 'todo'
urlpatterns = [
    path('',TodoModelView.as_view(),name='TodoModelView'),
    path('<int:pk>/',TodoModelDetailView.as_view(),name='TodoModelDetailView'),
]
