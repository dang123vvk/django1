from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemoListView.as_view(), name = 'index'),
    path('index', views.MemoListView.as_view(), name = 'index'),
    path('memo_create', views.MemoCreateView.as_view(), name = 'memo_create'),
    path('<int:pk>/memo_detail',
        views.MemoDetailView.as_view(), name = 'memo_detail'),
    path('<int:pk>/memo_update',
        views.MemoUpdateView.as_view(), name = 'memo_update'),
]