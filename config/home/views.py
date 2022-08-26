from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

import sys
sys.path.append(r'\config\home')

p=0
from .models import Person
list1=[' ',' ',' ',' ']
list2=[' ',' ',' ',' ']
list3=[' ',' ',' ',' ']
list4=[' ',' ',' ',' ']
list5=[' ',' ',' ',' ']
list6=[' ',' ',' ',' ']
list7=[' ',' ',' ',' ']
list8=[' ',' ',' ',' ']
list9=[' ',' ',' ',' ']
list10=[' ',' ',' ',' ']
list11=[' ',' ',' ',' ']
list12=[' ',' ',' ',' ']
list13=[' ',' ',' ',' ']
list14=[' ',' ',' ',' ']
list15=[' ',' ',' ',' ']
list16=[' ',' ',' ',' ']
list17=[' ',' ',' ',' ']
list18=[' ',' ',' ',' ']
list19=[' ',' ',' ',' ']


# ...
def index(request):
    rtot = Person.objects.order_by('-pub_date')
    r201 =rtot[72:]
    r202 =rtot[68:72]
    r203 =rtot[64:68]
    r204 =rtot[60:64]
    r205 =rtot[56:60]
    r206 =rtot[52:56]
    r207 =rtot[48:52]
    r208 =rtot[44:48]
    r209 =rtot[40:44]
    r210 =rtot[36:40]
    r211 =rtot[32:36]
    r212 =rtot[28:32]
    r213 =rtot[24:28]
    r214 =rtot[20:24]
    r215 =rtot[16:20]
    r216 =rtot[12:16]
    r217 =rtot[8:12]
    r218 =rtot[4:8]
    r101 =rtot[0:4]
    a=request.GET.get('time')
    if a==None:
        t = ' '
    else:
        t = request.GET.get('time')

    p = request.GET.get('per')
    if p == None:
        p== None
    else:
        p=int(p)
    c=0

    for person in r201:
        if person.id == p:
            list1[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r202:
        if person.id == p:
            list2[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r203:
        if person.id == p:
            list3[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r204:
        if person.id == p:
            list4[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r205:
        if person.id == p:
            list5[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r206:
        if person.id == p:
            list6[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r207:
        if person.id == p:
            list7[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r208:
        if person.id == p:
            list8[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r209:
        if person.id == p:
            list9[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r210:
        if person.id == p:
            list10[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r211:
        if person.id == p:
            list11[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r212:
        if person.id == p:
            list12[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r213:
        if person.id == p:
            list13[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r214:
        if person.id == p:
            list14[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r215:
        if person.id == p:
            list15[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r216:
        if person.id == p:
            list16[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r217:
        if person.id == p:
            list17[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r218:
        if person.id == p:
            list18[c]=t
            c=c+1
        else:
            c=c+1
    c=0

    for person in r101:
        if person.id == p:
            list19[c]=t
            c=c+1
        else:
            c=c+1
    c=0
    context = {'r201': r201,'r202' : r202,'r203' : r203,'r204' : r204,'r205' : r205,'r206' : r206,'r207' : r207,'r208' : r208,'r209' : r209,'r210' : r210,'r211' : r211,'r212' : r212,'r213' : r213,'r214' : r214,'r215' : r215,'r216' : r216,'r217' : r217,'r218' : r218,'r101' : r101,'c' : c, 'list1' : list1, 'list2' : list2, 'list3' : list3, 'list4' : list4, 'list5' : list5, 'list6' : list6, 'list7' : list7, 'list8' : list8, 'list9' : list9, 'list10' : list10, 'list11' : list11, 'list12' : list12, 'list13' : list13, 'list14' : list14, 'list15' : list15, 'list16' : list16, 'list17' : list17, 'list18' : list18, 'list19' : list19}
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(context, request))

def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'home/detail.html', {'person': person})
