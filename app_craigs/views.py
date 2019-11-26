from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from .models import Search

BASE_CRAIGS_URL = 'https://kenya.craigslist.org/search/sss?query={}'
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
	
	post_listing = soup.find_all('li', { 'class': 'result-row'})

	fina_postings = []
	for post in post_listing:
		post_title = post.find(class_ = 'result-title').text
		post_url = post.find('a').get('href')
		if post.find(class_='result-price'):
			post_price = post.find(class_='result-price').text
		else:
			post_price = 'N/A'

		if post.find(class_='result-image').get('data-ids'):
			post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
			post_image_url = BASE_IMAGE_URL.format(post_image_id)
			print(post_image_url)
		else:
			post_image_url = 'https://craigslist.org/images/peace.jpg'

		fina_postings.append((post_title, post_url, post_price, post_image_url))

	context_for_frontend = {
		'searched_item': searched_item,
		'final_postings': fina_postings
	}
	return render(request, 'app_craigs/new_search.html', context_for_frontend)