# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from DIRCongCards.models import Congresman


def home(request):
    if request.GET:
        try:
            fullName = request.GET['congresista']
            name = fullName.split('__')[0]
            name = name.split('_')
            name = ' '.join(name)

            lastname = fullName.split('__')[1]
            lastname = lastname.split('_')
            lastname = ' '.join(lastname)
            CONGRESMAN = Congresman.objects.all()
            CONGRESMAN = CONGRESMAN.filter(NOMBRE=name)
            CONGRESMAN = CONGRESMAN.filter(APELLIDOS=lastname)

            CONGRESMAN = CONGRESMAN.values()

            CONGRESMAN = {
                'CONGRESMAN': CONGRESMAN[0],
            }

            return render_to_response('detail.html', CONGRESMAN)

        except Exception as e:
            print(e)
            return render_to_response('404.html')
    else:
        pass
    CONGRES = {
        'CONGRES': [
            CONGRESMAN.getData() for CONGRESMAN in Congresman.objects.all()
        ]
    }

    return render_to_response('home.html', CONGRES)
