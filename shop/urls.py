from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
	path('', views.shop, name="home"),

	path('single-product/<int:id>/', views.single_product, name="single-product"),

	path('product-categorie', views.product_categorie, name="product-categorie"),





	path('cart', views.cart, name="cart"),

	path('checkout', views.checkout, name="checkout"),

	path('my-account', views.account, name="my-account"),


	path('shop-list', views.shop_list, name="shop-list"),


	path('wishlist', views.wishlist, name="wishlist"),
    
]
