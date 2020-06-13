from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
	path('cart', views.cart, name="cart"),
	path('chechout', views.chechout, name="chechout"),
	path('my-account', views.account, name="my-account"),
	path('product-categorie', views.product_categorie, name="product-categorie"),
	path('shop-list', views.shop_list, name="shop-list"),
	path('shop', views.shop, name="shop"),
	path('single-product', views.single_product, name="single-product"),
	path('wishlist', views.wishlist, name="wishlist"),
    
]
