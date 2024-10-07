from django.urls import path

from products.views import ProductListView , ProductDetailView,FileListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path ('files/<int:p_id>/', FileListView.as_view(), name='files-list'),
]