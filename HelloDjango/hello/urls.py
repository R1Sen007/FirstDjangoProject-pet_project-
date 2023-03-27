from django.urls import path, include
# from hello import views as hello_views
from .views import ShopListView, ShopDetailView, ShopCreateView, AdressCreateView, ShopUpdateView, ProductCreateView, ProductUpdateView, ProductDeleteView


urlpatterns = [
        # path('', hello_views.index, name='home'),
        path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
        path('shop/<int:pk>/update/', ShopUpdateView.as_view(), name='shop-update'),
        path('shop/<int:shop_pk>/product/create/', ProductCreateView.as_view(), name='product-create'),
        path('shop/<int:shop_pk>/product/<int:product_pk>/update/', ProductUpdateView.as_view(), name='product-update'),
        path('shop/<int:shop_pk>/product/<int:product_pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
        path('shop/new/', ShopCreateView.as_view(), name='shop-create'),
        path('shop/adress/create/', AdressCreateView.as_view(), name='adress-create'),
        path('', ShopListView.as_view(), name='home')
]