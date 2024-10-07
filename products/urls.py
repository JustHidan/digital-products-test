from django.urls import path

from products.views import (
    ProductListView , ProductDetailView,FileListView,
    FileDetailView,CategoryListView,CategoryDetailView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path ('products/files/<int:p_id>/', FileListView.as_view(), name='files-list'),
    path ('products/files/<int:p_id>/<int:f_id>/' , FileDetailView.as_view(), name='files-detail'),

    path ('category/' , CategoryListView.as_view(), name='category-list'),
    path ('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]