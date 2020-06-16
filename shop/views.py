from django.shortcuts import render
from . import models
from electro.models import Info
from django.core.paginator import Paginator
# Create your views here.

# lien → {% url 'shop:home' %}
def shop(request):

	productList = models.Product.objects.all()
	paginator = Paginator(productList, 10) # affiche 10 produits per page

	page = request.GET.get('page')
	produits = paginator.get_page(page)

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

	return render(request, "shop/shop.html",data,produits)



# lien → {% url 'shop:single-product' %}
def single_product(request, id):

	data = {
		'article': models.Product.objects.get(id=id),
		# 'recents': models.Article.objects.filter(date_pub__gte=date),
		# 'comment': models.Commentaire.objects.filter(article_id=id).filter(status=True)
	}

	return render(request, "shop/single-product-fullwidth.html",data)

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

