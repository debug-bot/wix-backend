from django.urls import path
from .views import TemplateListCreateView, WebsiteListCreateView, PageListCreateView, WebsiteDetailAPIView

urlpatterns = [
    path('templates/', TemplateListCreateView.as_view(), name='template-list'),
    path('websites/', WebsiteListCreateView.as_view(), name='website-list'),
    path('websites/<int:pk>/', WebsiteDetailAPIView.as_view(), name='website-detail'),
    path('pages/', PageListCreateView.as_view(), name='page-list'),
]
