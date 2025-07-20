from django.urls import path
from products.views import BulkDeleteProductsView, CreateProductView, DeleteProductView, ProductListView, RetrieveProductView, UpdateProductView
from products.service import ImportFakeStoreProductsView

urlpatterns = [
    path('import-products', ImportFakeStoreProductsView.as_view()),
    path('product-list', ProductListView.as_view()),
    path('create-product', CreateProductView.as_view()),
    path('product-details', RetrieveProductView.as_view()),
    path('update-product', UpdateProductView.as_view()),
    path('delete-product', DeleteProductView.as_view()),
    path('bulk-delete-products', BulkDeleteProductsView.as_view()),
]