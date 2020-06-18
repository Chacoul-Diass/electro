from django.shortcuts import render
from . import models
from electro.models import Info
from django.core.paginator import Paginator
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

	'products' : models.Product.objects.all(),

	'info':Info.objects.first(),
	}

	return render(request, "shop/shop.html",data)



# lien → {% url 'shop:single-product' %}
def single_product(request, id):

	data = {
		'article': models.Product.objects.get(id=id),

		'info':Info.objects.first(),
	}

	return render(request, "shop/single-product-fullwidth.html",data)
