"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from store_admin_app.views import IndexView


urlpatterns = [
	path('admin/', admin.site.urls),
	path('product/', include('products.urls')),
	path('order/', include('orders.urls')),
	url(r'^store/', include('store_app.urls', namespace='store-app-namespace')),
	url(r'^account/', include('account.urls', namespace='account-namespace')),
	url(r'^store-admin/', include('store_admin_app.urls', namespace='store-admin-app-namespace')),
	url(r'^$', IndexView, name='website'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
