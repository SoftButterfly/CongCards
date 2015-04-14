from django.contrib import admin

from DIRCongCards.models import Congresman


class CongresmanAdmin(admin.ModelAdmin):
    search_fields = (
        'NOMBRE',
        'APELLIDOS',
        'REGION',
        'BANCADA',
    )

    list_display = (
        'NOMBRE',
        'APELLIDOS',
        'RETRATO',
        'CARGO',
        'REGION',
        'BANCADA',
        'PAGINA_WEB',
        'PAGINA_WEB2',
        'EMAIL_1',
        'EMAIL_2',
        'EMAIL_3',
        'DIRECCION_LIMA',
        'DISTRITO_LIMA',
        'PROVINCIA_LIMA',
        'DIRECCION_REGION',
        'DISTRITO_REGION',
        'PROVINCIA_REGION',
        'TELEFONO_LIMA_1',
        'TELEFONO_LIMA_2',
        'TELEFONO_CELULAR',
        'TELEFONO_REGION_1',
        'TELEFONO_REGION_2',
        'TELEFONO_REGION_3',
        'TWITTER',
        'FACEBOOK',
        'GOOGLEP',
        'YOUTUBE',
        'BLOG',
        'FLICKR',
        'ISSUU',
        'IBLUPS',
        'OTROS',
        'PROYECTO_LEY',
    )


admin.site.register(Congresman, CongresmanAdmin)
