from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST.get('input_url',False) #get userinput if nothing then print default = False
        print(url)
        input_url = requests.get(url).text  #take all the element of html as raw text
        soup = BeautifulSoup(input_url, 'html.parser')
        # print(soup.prettify())
        var_html = {
            'src_code' : soup.prettify(),
            'title': soup.title.string,
            'all_link': soup.find_all('a'), 
            'all_text': soup.get_text(),
        }
        return render(request, 'index.html', var_html) #passing variable dictionary to render to use variable in html if user enters the URL
    return render(request, 'index.html')  #no URL passed no var_html assigned hence return index page


'''
REMEMBER
---------------
The “TypeError: 'method' object is not subscriptable” error is raised when you use square 
brackets to call a method inside a class. To solve this error, make sure that you only call
 methods of a class using curly brackets after the name of the method you want to call
'''