from django.urls import path

from . import views


urlpatterns = [
    path('',  views.ProductListCreateApiView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view()),  # /api/products/123
    path('<int:pk>/', views.ProductDetailApiView.as_view()),  # /api/products/123
    path('<int:pk>/delete/', views.ProductDestroyApiView.as_view()),  # /api/products/123

]