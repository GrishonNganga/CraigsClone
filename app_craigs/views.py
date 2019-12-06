from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from .models import Search

BASE_JUMIA_URL = 'https://www.jumia.co.ke/catalog/?q={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
def home_view(request):
	return render(request, 'base.html', {})

def new_search_view(request):
	searched_item = request.POST.get('search')
	Search.objects.create(search_field = searched_item)
	final_url = BASE_CRAIGS_URL.format(quote_plus(searched_item))
	print(final_url)
	response = requests.get(final_url)
	data = response.text
	soup = BeautifulSoup(data, features = 'html.parser')
	
	post_listing = soup.find_all({ 'class': 'products osh_gallery-no_gutter'})

	fina_postings = []
	for post in post_listing:
		post_title = post.find(class_ = 'text text-title -align-left -mbxs -ellipsis-2').text
		post_url = post.find('a').get('href')
		if post.find(class_='text text-body-1 color-default -mrxs -inline-block js-actual-price'):
			friday_pirce = post.find(class_='text text-body-1 color-default -mrxs -inline-block js-actual-price').text
			post_price = post.find(class_='text text-caption-default-800 -strike -inline-block -mrxs js-old-price').text
		else:
			post_price = 'N/A'

		if post.find(class_='lazy card-sku_list--image -block-center -loaded')
			post_image_id = 
			post_image_url = post.find(class_='lazy card-sku_list--image -block-center -loaded').text
			print(post_image_url)
		else:
			post_image_url = 'https://craigslist.org/images/peace.jpg'

		fina_postings.append((post_title, post_url, post_price, post_image_url))

	context_for_frontend = {
		'searched_item': searched_item,
		'final_postings': fina_postings
	}
	return render(request, 'app_craigs/new_search.html', context_for_frontend)