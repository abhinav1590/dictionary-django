from django.shortcuts import redirect, render
from django.core.exceptions import BadRequest
from bs4 import BeautifulSoup
import requests

def home(request):
    if request.method == 'POST':
        word = request.POST['word']
        url = 'https://www.dictionary.com/browse/'+word
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')
        span = soup.find_all('span',{'class':'one-click-content'})

        if len(span) != 0:
            return render(request, 'index.html',{
                'text': span[0].text,
                'word': word.upper() })
        else:
            return render(request,'index.html',{'error_message': "Enter a valid text"})
    else:
        return render(request,'index.html')






