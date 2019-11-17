from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models
BASE_CRAGLIST_URL = 'https://bangladesh.craigslist.org/search/eee?query={}'
# Create your views here.
def home(request):
    return render(request,'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    #print(search)
    final_url = BASE_CRAGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    text = response.next
    soup = BeautifulSoup(text, features='html.parser')
    post_title = soup.findall('a',{'class':'result-title'})
    post_title = soup.findall('a',{'class':'result-title'})
    print(post_title)

    stuff_for_fronted ={
        'search':search
    }
    return render(request,'my_app/new_search.html',stuff_for_fronted)



