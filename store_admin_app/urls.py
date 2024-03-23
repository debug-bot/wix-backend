from django.contrib import admin
from django.urls import re_path
from .views import *

app_name = 'store_admin_app'

urlpatterns = [
	re_path(r'^index/$',IndexView ,name='index-view'),
	re_path(r'^login/$',LoginView ,name='login-view'),
	re_path(r'^logout/$',LogoutView ,name='logout-view'),
	re_path(r'^categories/$',CategoriesView ,name='categories-view'),
	re_path(r'^collections/$',CollectionsView ,name='collections-view'),
	re_path(r'^coupons/$',CuponsListView ,name='coupon-view'),
	re_path(r'^orders/$',OrdersView ,name='orders-view'),
	re_path(r'^products/$',ProductsView ,name='products-view'),
	re_path(r'^custom-colors/$',CustomColorsView ,name='custom-colors-view'),
	re_path(r'^category/create/$',CreateCategoryView ,name='category-create-view'),
	re_path(r'^collection/create/$',CreateCollectionView ,name='collection-create-view'),
	re_path(r'^product/create/$',CreateProductView ,name='product-create-view'),
	re_path(r'^coupon/create/$',CuponsCreatelView ,name='coupon-create-view'),
	re_path(r'^custom-colors/create/$',CreateCustomColorsView ,name='custom-colors-create-view'),
	re_path(r'^category/crud/(?P<id>[0-9]+)/$',CategoryCRUDView ,name='category-crud-view'),
	re_path(r'^collection/crud/(?P<id>[0-9]+)/$',CollectionCRUDView ,name='collection-crud-view'),
	re_path(r'^coupon/crud/(?P<id>[0-9]+)/$',CuponCRUDView ,name='coupon-crud-view'),
	re_path(r'^order/(?P<id>[0-9]+)/$',OrderDetailView ,name='order-detail-view'),
	re_path(r'^product/crud/(?P<id>[0-9]+)/$',ProductCRUDView ,name='product-crud-view'),
	re_path(r'^custom-colors/crud/(?P<id>[0-9]+)/$',CustomColorsCRUDView ,name='custom-colors-crud-view'),
]
