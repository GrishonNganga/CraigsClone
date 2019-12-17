from django.urls import path
from .views import home_view, new_search_view, at_view

urlpatterns = [
	path('', home_view, name = 'home_view'),
	path('new_search', new_search_view, name = 'new_search_view' ),
	path('at', at_view, name = 'at'),
]