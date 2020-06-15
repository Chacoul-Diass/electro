from django.shortcuts import render
from . import models

# Create your views here.

# lien → {% url 'shop:home' %}
def shop(request):
	data = {
	# tous les departements
	'departements':models.Departement.objects.all(),

	# les 5 derniers produits en ordre decroissant de id
	'latestProds':models.Product.objects.reverse()[:5],

	'recomProds':models.Product.objects.filter(recommande=True).reverse()[:10],

	'nbArticles':models.Product.objects.count(),
	}
	return render(request, "shop/shop.html",data)

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

