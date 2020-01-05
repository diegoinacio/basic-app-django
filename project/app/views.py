from django.shortcuts import render

from .models import Person, MailList

# Create your views here.


MENU = [
    {'title': 'Home page', 'page': 'home'},
    {'title': 'About', 'page': 'about'},
    {'title': 'Contact', 'page': 'contact'}
]


def home(request):
    TITLE, PAGE = MENU[0]['title'], MENU[0]['page']
    return render(request, f'{PAGE}.html', {'TITLE': TITLE, 'MENU': MENU})

def about(request):
    TITLE, PAGE = MENU[1]['title'], MENU[1]['page']
    ############
    # Database #
    ############
    PEOPLE = [{
        'name': person.name,
        'title': person.title,
        'desc': person.descript,
        'email': person.email,
        'img': person.img
    } for person in Person.objects.all()]
    return render(request, f'{PAGE}.html', {'TITLE': TITLE, 'MENU': MENU, 'PEOPLE': PEOPLE})

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        ml = MailList(fullname=fullname, email=email)
        ml.save()
        print(f'{fullname} was added to the mailing list!')
    TITLE, PAGE = MENU[2]['title'], MENU[2]['page']
    return render(request, f'{PAGE}.html', {'TITLE': TITLE, 'MENU': MENU})
