from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request, 'base.html', {})

def new_search_view(request):
	searched_item = request.POST.get('search')
	context_for_frontend = {
		'searched_item': searched_item
	}
	return render(request, 'app_craigs/new_search.html', context_for_frontend)