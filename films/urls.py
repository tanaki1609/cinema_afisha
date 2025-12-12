from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list_create_api_view),
    path('<int:id>/', views.film_detail_api_view),
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('genres/', views.GenreViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('genres/<int:id>/', views.GenreViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    }))
]
