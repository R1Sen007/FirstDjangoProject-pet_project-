from django.urls import path, include
# from hello import views as hello_views
from .views import ShopListView, ShopDetailView


urlpatterns = [
        # path('', hello_views.index, name='home'),
        path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
        path('', ShopListView.as_view(), name='home')
]