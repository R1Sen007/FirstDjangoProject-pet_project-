"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from hello import views as hello_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

# products_patterns = [
#     path("", views.products),
#     path("new", views.new),
#     path("top", views.top),
# ]

# product_atribute = [
#     path("", views.product),
#     path("comments", views.comments),
#     path("questions", views.questions)
# ]

# urlpatterns = [
#     path('', views.index),
#     path("create/", views.create),
#     path("edit/<int:id>/", views.edit),
#     path("delete/<int:id>/", views.delete),
#     path("postuser/", views.postuser),
#     path("user", views.user),
#     path("products/<int:id>/", include(product_atribute)),
#     path("products/", include(products_patterns)),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signin/', user_views.register, name='signin'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/update/', user_views.update, name='update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
