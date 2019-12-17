from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from .models import Search

BASE_JUMIA_URL = 'https://www.jumia.co.ke/catalog/?q={}'

# Create your views here.
def home_view(request):
	return render(request, 'base.html', {})

def new_search_view(request):
	searched_item = request.POST.get('search')
	Search.objects.create(search_field = searched_item)
	final_url = BASE_JUMIA_URL.format(quote_plus(searched_item))
	print("Comes next")
	print(final_url)
	response = requests.get(final_url)
	data = response.text
	soup = BeautifulSoup(data, features = 'html.parser')
	post_listing = soup.find_all("a", {'class': 'link'} )

	biggest = 0;
	fina_postings = []
	for post in post_listing:
		post_title = post.find("span", {'class': 'name'})
		post_title_text = post_title.text
		print(post)
		#print(post_title)
		#first_div = post_title.next_sibling
		#print(first_div)
		post_url = post.get('href')

		if post.find("span", {'class': 'price'}):
			post_price = post.find_all("span", {'class': 'price'})
			priceEnd = post_price[0].text
		else:
			priceEnd = 'N/A'

		if post.find("span", {'class': 'price -old'}):
			old_post_price = post.find_all("span", {'class': 'price -old'})
			old_priceEnd = old_post_price[0].text
		else:
			old_priceEnd = 'N/A'

		big = [int(s) for s in old_priceEnd.split() if s.isdigit()]
		small = [int(s) for s in priceEnd.split() if s.isdigit()]

		print(big)
		if big and small:
			bigg = big[0]
			smal = small[0]
			net = bigg - smal
			if net > biggest:
				biggest = net

				if post.find('noscript', class_ = 'image'):
					post_image_url = post.find('noscript', class_ = 'image')
					src = post_image_url.get('src');
					print(src)
				else:
					post_image_url = 'https://craigslist.org/images/peace.jpg'
		elif small and not big:
			print("Not valid")
		else:
			post_image_url = 'https://craigslist.org/images/peace.jpg'
			post_title_text = "N/A"
			priceEnd = "N/A"


		print(biggest)

		
		

	fina_postings.append((post_title_text, post_url, priceEnd, post_image_url))

	context_for_frontend = {
		'searched_item': searched_item,
		'final_postings': fina_postings
	}
	return render(request, 'app_craigs/new_search.html', context_for_frontend)

	def at_view(request):
		if request.method == POST:
			sessionId = request.POST.get("sessionId")
			service_code = request.POST.get("serviceCode")
			phone_number = request.POST.get("phoneNumber")
  			text = request.POST.get("text")
			print(sessionId)
			print(service_code)
			print(phone_number)
			print(text)
