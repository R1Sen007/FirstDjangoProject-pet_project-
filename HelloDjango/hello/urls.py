from django.urls import path, include
# from hello import views as hello_views
from .views import ShopListView, ShopDetailView, ShopCreateView, AdressCreateView


urlpatterns = [
        # path('', hello_views.index, name='home'),
        path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
        path('shop/new/', ShopCreateView.as_view(), name='shop-create'),
        path('shop/adress/create', AdressCreateView.as_view(), name='adress-create'),
        path('', ShopListView.as_view(), name='home')
]