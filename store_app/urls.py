from django.urls import re_path
from .views import *
from django.urls import path


app_name = 'store_app'

urlpatterns = [
	re_path(r'^categories/$',CategoryListView.as_view(),name='category-list-view'),
	re_path(r'^categories/men/$',CategoryMenListView.as_view(),name='category-list-men-view'),
	re_path(r'^categories/women/$',CategoryWomenListView.as_view(),name='category-list-women-view'),
	re_path(r'^collections/$',CustomCollectionListView.as_view(),name='collection-list-view'),
	re_path(r'^collections/men/$',CustomCollectionMenListView.as_view(),name='collection-list-men-view'),
	re_path(r'^collections/women/$',CustomCollectionWomenListView.as_view(),name='collection-list-woman-view'),
	re_path(r'^category/title/(?P<title>[\w\-]+)/$',CategoryTitleDetailView.as_view(),name='category-title-view'),
	re_path(r'^category/title/men/(?P<title>[\w\-]+)/$',CategoryTitleMenDetailView.as_view(),name='category-title-view'),
	re_path(r'^category/title/women/(?P<title>[\w\-]+)/$',CategoryTitleWomenDetailView.as_view(),name='category-title-view'),
	re_path(r'^collection/title/(?P<title>[\w\-]+)/$',CustomCollectionTitleDetailView.as_view(),name='collection-title-view'),
	re_path(r'^products-extra-tags/$',ProductsPerExtraTag.as_view(),name='products-extra-tags-list-view'),
	re_path(r'^collections/(?P<id>[0-9]+)/$',CustomCollectionDetailView.as_view(),name='collection-list-view'),
	re_path(r'^product-images/(?P<id>[0-9]+)/$', ProductImagesView.as_view(), name='product-images-detail-api'),
	re_path(r'^categories/(?P<id>[0-9]+)/$', CategoryDetailView.as_view(), name='category-detail-api'),
	re_path(r'^products/$',ProductListView.as_view(),name='products-list-view'),
	re_path(r'^products/(?P<id>[0-9]+)/$', ProductDetailView.as_view(), name='products-detail-api'),
	re_path(r'^cart/(?P<token>[0-9A-Za-z_\-]+)/$',CartView.as_view(),name='cart-detail-view'),
	re_path(r'^cart/$',CartView.as_view(),name='cart-view'),
	re_path(r'^cart/delete-product/(?P<id>[0-9]+)/$', ProductVariationView.as_view(), name='delete-product-api'),
	re_path(r'^custom-products/$',ProductVariationListView.as_view(),name='custom-products-list-view'),
	re_path(r'^custom-products/(?P<id>[0-9]+)/$', ProductVariationView.as_view(), name='custom-products-detail-api'),
	re_path(r'^order/(?P<cart_token>[0-9A-Za-z_\-]+)/$', CheckoutView.as_view(), name='checkout-detail-api'),
	re_path(r'^shipping-info/(?P<cart_token>[0-9A-Za-z_\-]+)/$', ShippingInfoView.as_view(), name='checkout-detail-api'),
	re_path(r'^checkout-paypal/(?P<cart_token>[0-9A-Za-z_\-]+)/$', OderCheckoutPaypalView.as_view(), name='checkout-detail-api'),
	re_path(r'^coupon/(?P<token>[0-9A-Za-z_\-]+)/$', AddCoupon.as_view(), name='coupon-add-api'),
    # add website detail with id re_path
    path('website/<int:user_id>/<int:template_id>/', WebsiteTemplateDetail.as_view(), name='website-template-detail'),
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
    path('templates/', AllTemplateView.as_view(), name='templates'),
    path('templates/<int:template_id>/', GetTemplateView.as_view(), name='templates-id'),
    path('user-template/<int:user_id>/', UserTemplateView.as_view(), name='user-template'),
    path('user-template-detail/<int:user_id>/<int:user_template_id>/', UserTemplateDetailView.as_view(), name='user-template-detail'),
    path('post-user-template/', PostUserTemplateView.as_view(), name='post-user-template'),
    path('editor-template/<int:user_id>/<int:temp_id>/', EditorUserTemplateDetailView.as_view(), name='editor-template'),
    path('qrcode-history/', QrcodeView.as_view(), name='qrcode-history'),
]
