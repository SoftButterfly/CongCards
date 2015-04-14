# -*- coding: utf-8 -*-
from Directory.models import Congresman
import django

django.setup()

fileName = './directory.csv'
fileHandler = open(fileName, 'r')

CongresmanDict = dict({
    'NOMBRE': '',
    'APELLIDOS': '',
    'CARGO': '',
    'REGION': '',
    'PAGINA_WEB': '',
    'PAGINA_WEB2': '',
    'EMAIL_1': '',
    'EMAIL_2': '',
    'EMAIL_3': '',
    'DIRECCION_LIMA': '',
    'DISTRITO_LIMA': '',
    'PROVINCIA_LIMA': '',
    'DIRECCION_REGION': '',
    'DISTRITO_REGION': '',
    'PROVINCIA_REGION': '',
    'TELEFONO_LIMA_1': '',
    'TELEFONO_LIMA_2': '',
    'TELEFONO_CELULAR': '',
    'TELEFONO_REGION_1': '',
    'TELEFONO_REGION_2': '',
    'TELEFONO_REGION_3': '',
    'TWITTER': '',
    'FACEBOOK': '',
    'GOOGLEP': '',
    'YOUTUBE': '',
    'BLOG': '',
    'FLICKR': '',
    'ISSUU': '',
    'IBLUPS': '',
    'OTROS': '',
    'PROYECTO_LEY': '',
})

for line in fileHandler:
    tokens = line.split("\",\"")
    CongresmanDict['NOMBRE'] = tokens[1]
    CongresmanDict['APELLIDOS'] = tokens[2]
    CongresmanDict['CARGO'] = tokens[3]
    CongresmanDict['REGION'] = tokens[4]
    CongresmanDict['PAGINA_WEB'] = tokens[5]
    CongresmanDict['PAGINA_WEB2'] = tokens[6]
    CongresmanDict['EMAIL_1'] = tokens[7]
    CongresmanDict['EMAIL_2'] = tokens[8]
    CongresmanDict['EMAIL_3'] = tokens[9]
    CongresmanDict['DIRECCION_LIMA'] = tokens[10]
    CongresmanDict['DISTRITO_LIMA'] = tokens[11]
    CongresmanDict['PROVINCIA_LIMA'] = tokens[12]
    CongresmanDict['DIRECCION_REGION'] = tokens[13]
    CongresmanDict['DISTRITO_REGION'] = tokens[14]
    CongresmanDict['PROVINCIA_REGION'] = tokens[15]
    CongresmanDict['TELEFONO_LIMA_1'] = tokens[16]
    CongresmanDict['TELEFONO_LIMA_2'] = tokens[17]
    CongresmanDict['TELEFONO_CELULAR'] = tokens[18]
    CongresmanDict['TELEFONO_REGION_1'] = tokens[19]
    CongresmanDict['TELEFONO_REGION_2'] = tokens[20]
    CongresmanDict['TELEFONO_REGION_3'] = tokens[21]
    CongresmanDict['TWITTER'] = tokens[22]
    CongresmanDict['FACEBOOK'] = tokens[23]
    CongresmanDict['GOOGLEP'] = tokens[23]
    CongresmanDict['YOUTUBE'] = tokens[25]
    CongresmanDict['BLOG'] = tokens[26]
    CongresmanDict['FLICKR'] = tokens[27]
    CongresmanDict['ISSUU'] = tokens[28]
    CongresmanDict['IBLUPS'] = tokens[29]
    CongresmanDict['OTROS'] = tokens[30]
    CongresmanDict['PROYECTO_LEY'] = tokens[31]
    c = Congresman(**CongresmanDict)
    c.save()
    print c.__str__()
