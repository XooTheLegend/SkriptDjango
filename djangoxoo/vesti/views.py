from django.shortcuts import render
from django.http import HttpResponse
from .models import Vesti, Korisnici, Komentari, Cookies

def index(request, x=0):
    tmp = Vesti.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        tmp = Vesti.objects.filter(content__icontains=q) | Vesti.objects.filter(title__icontains=q)

    elif 'date' in request.GET:
        #request.GET.get('date')
        order = request.GET['date']
        if order == 'ASC':
            tmp = Vesti.objects.all().order_by('date')
        elif order == 'DSC':
            tmp = Vesti.objects.all().order_by('-date')

    elif 'sort' in request.GET:
        #request.GET.get('sort')
        order = request.GET['sort']
        if order == 'ASC':
            tmp = Vesti.objects.all().order_by('count')
        elif order == 'DSC':
            tmp = Vesti.objects.all().order_by('-count')

    elif 'kategorija' in request.GET:
        request.GET.get('kategorija')
        kategorija = request.GET['kategorija']
        tmp = Vesti.objects.filter(category=kategorija)

    for vest in tmp:
        x += vest.count

    f = []
    for vest in Vesti.objects.all():
        if vest.category in f:
            continue
        else:
            f.append(vest.category)

    g = {}
    for vest in Vesti.objects.all():
        if vest.id in g:
            continue
        else:
            g[vest.id] = 0

    for vest in Vesti.objects.all():
        for komentar in Komentari.objects.all():
            if komentar.news == vest.id:
                g[vest.id] += 1

    return render(request, 'vesti.html', {'vesti':tmp, 'x':x, 'kategorije':f, 'komentari':g})

def korisnici(request):
    tmp = Korisnici.objects.all()

    if 'name' in request.GET:
        name = request.GET['name']
        tmp = Korisnici.objects.filter(name__icontains=name)

    elif 'surname' in request.GET:
        surname = request.GET['surname']
        tmp = Korisnici.objects.filter(surname__icontains=surname)

    elif 'type' in request.GET:
        type = request.GET['type']
        tmp = Korisnici.objects.filter(tip__icontains=type)

    admins = 0
    creators = 0
    for korisnik in Korisnici.objects.all():
        if korisnik.tip == 'ADMIN':
            admins += 1
        if korisnik.tip == 'CONTENT_CREATOR':
            creators += 1

    o = []

    for guest in Cookies.objects.all():
        if guest.value in o:
            continue
        else:
            o.append(guest.value)

    guests = len(o)

    return render(request, 'korisnici.html', {'korisnici':tmp, 'admins':admins, 'creators':creators, 'guests':guests})

def komentari(request):
    tmp = Komentari.objects.all()
    maxi = 0
    maxKomentar = None
    for komentar in tmp:
        if komentar.likes > maxi:
            maxi = komentar.likes
            maxKomentar = Komentari.objects.get(id=komentar.id)

    lajkovi = 0
    for komentar in tmp:
        lajkovi += komentar.likes

    d = {}
    for komentar in tmp:
        if komentar.news in d:
            d[komentar.news] += 1
        else:
            d[komentar.news] = 1

    max_value = max(d.values())
    max_key = None
    for k,v in d.items():
        if v == max_value:
            max_key = k
    print(max_key)

    n = Vesti.objects.get(id=max_key)

    return render(request, 'komentari.html', {'komentari':tmp,'lajkovi':lajkovi,'maxKomentar':maxKomentar,
                                              'brKomentara':max_value, 'vest':n})

def broj(request,br):
    return HttpResponse('Broj: ' + str(br))

def query(request):
    return HttpResponse('Params: ' + request.GET.get('ime', ''))

def regex(request, godina, mesec):
    return HttpResponse('Godina: ' + godina + 'Mesec: ' + mesec)
