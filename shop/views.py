from django.shortcuts import render

# Create your views here.

def cart(request):
	return render(request, "shop/cart.html")

def checkout(request):
	return render(request, "shop/checkout.html")

def account(request):
	return render(request, "shop/my-account.html")

def product_categorie(request):
	return render(request, "shop/product-categorie.html")

def shop-list(request):
	return render(request, "shop/shop-list.html")

def shop(request):
	return render(request, "shop/shop.html")

def single_product(request):
	return render(request, "shop/single-product.html")

def wishlist(request):
	return render(request, "shop/single-product.html")
