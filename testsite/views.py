from django.http import HttpResponse 
from django.shortcuts import render

data = {
    'testsite':[
        {
            'id': 4,
            'location': 'Stella',
            'year': 2000,


        },
        {
            'id': 8,
            'location': 'HomeWorking',
            'year': 2020,

        },

        {
            'id': 9,
            'location': 'Bridge House',
            'year': 2021,


        }

    
    
    ]
}

def testsite(request):
    return render(request, 'testsite/testsite.html', data)


def home(request):
    return HttpResponse("Home page")


