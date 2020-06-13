from django.shortcuts import render

# Create your views here.

# lien → {% url 'shop:home' %}
def shop(request):
	return render(request, "shop/shop.html")

# lien → {% url 'shop:single-product' %}
def single_product(request):
	return render(request, "shop/single-product-fullwidth.html")

# lien → {% url 'shop:product-categorie' %}
def product_categorie(request):
	return render(request, "shop/product-categorie.html")




def cart(request):
	return render(request, "shop/cart.html")

def checkout(request):
	return render(request, "shop/checkout.html")

def account(request):
	return render(request, "shop/my-account.html")

def shop_list(request):
	return render(request, "shop/shop-list.html")


def wishlist(request):
	return render(request, "shop/single-product.html")

