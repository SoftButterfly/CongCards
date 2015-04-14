# -*- coding: utf-8 -*-
from django.db import models

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Objetos definidos:
#     * Congresman

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Tablas de la base de datos
TABLES = {
    'Congresman': 'congresman_table',
}


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Congresista
class Congresman(models.Model):
    NOMBRE = models.CharField(
        max_length=128
    )

    APELLIDOS = models.CharField(
        max_length=128
    )

    RETRATO = models.ImageField(
        upload_to='Retratos/',
        blank=True,
        null=True
    )

    CARGO = models.CharField(
        max_length=256
    )

    AMAZONAS = 'Amazonas'
    ANCASH = 'Áncash'
    APURIMAC = 'Apurímac'
    AREQUIPA = 'Arequipa'
    AYACUCHO = 'Ayacucho'
    CAJAMARCA = 'Cajamarca'
    CALLAO = 'Callao'
    CUZCO = 'Cuzco'
    HUANCAVELICA = 'Huancavelica'
    HUANUCO = 'Huánuco'
    ICA = 'Ica'
    JUNIN = 'Junín'
    LAMBAYEQUE = 'Lambayeque'
    LIMA = 'Lima'
    LORETO = 'Loreto'
    MOQUEGUA = 'Moquegua'
    PASCO = 'Pasco'
    PIURA = 'Piura'
    PUNO = 'Puno'
    TACNA = 'Tacna'
    TUMBES = 'Tumbes'
    UCAYALI = 'Ucayali'
    LA_LIBERTAD = 'La Libertad'
    MADRE_DE_DIOS = 'Madre de Dios'
    SAN_MARTIN = 'San Martín'

    REGIONES = (
        (AMAZONAS, 'Amazonas'),
        (ANCASH, 'Áncash'),
        (APURIMAC, 'Apurímac'),
        (AREQUIPA, 'Arequipa'),
        (AYACUCHO, 'Ayacucho'),
        (CAJAMARCA, 'Cajamarca'),
        (CALLAO, 'Callao'),
        (CUZCO, 'Cuzco'),
        (HUANCAVELICA, 'Huancavelica'),
        (HUANUCO, 'Huánuco'),
        (ICA, 'Ica'),
        (JUNIN, 'Junín'),
        (LAMBAYEQUE, 'Lambayeque'),
        (LIMA, 'Lima'),
        (LORETO, 'Loreto'),
        (MOQUEGUA, 'Moquegua'),
        (PASCO, 'Pasco'),
        (PIURA, 'Piura'),
        (PUNO, 'Puno'),
        (TACNA, 'Tacna'),
        (TUMBES, 'Tumbes'),
        (UCAYALI, 'Ucayali'),
        (LA_LIBERTAD, 'La Libertad'),
        (MADRE_DE_DIOS, 'Madre de Dios'),
        (SAN_MARTIN, 'San Martín'),
    )

    REGION = models.CharField(
        max_length=64,
        choices=REGIONES
    )

    ACCION_POPULAR = 'Acción Popular'
    ALIANZA_PARA_EL_PROGRESO = 'Alianza para el Progreso'
    DEMOCRACIA_DIRECTA = 'Democracia Directa'
    EL_FRENTE_AMPLIO_POR_JUSTICIA = 'El Frente Amplio por Justicia'
    FUERZA_POPULAR = 'Fuerza Popular'
    PARTIDO_APRISTA_PERUANO = 'Partido Aprista Peruano'
    PARTIDO_DEMOCRATICO_SOMOS_PERU = 'Partido Democrático Somos Perú'
    PARTIDO_HUMANISTA_PERUANO = 'Partido Humanista Peruano'
    PARTIDO_NACIONALISTA_PERUANO = 'Partido Nacionalista Peruano'
    PARTIDO_POLITICO_ORDEN = 'Partido Político Orden'
    PARTIDO_POPULAR_CRISTIANO = 'Partido Popular Cristiano-PPC'
    PERU_MAS = 'Perú Más'
    PERU_PATRIA_SEGURA = 'Perú Patria Segura'
    PERU_POSIBLE = 'Perú Posible'
    PERU_POSIBLE = 'Perú Posible'
    RESTAURACION_NACIONAL = 'Restauración Nacional'
    SIEMPRE_UNIDOS = 'Siempre Unidos'
    SOLIDARIDAD_NACIONAL = 'Solidaridad Nacional'
    TIERRA_Y_LIBERTAD = 'Tierra y Libertad'
    TODOS_POR_EL_PERU = 'Todos por el Perú'
    UNION_POR_EL_PERU = 'Unión por el Perú'
    VAMOS_PERU = 'Vamos Perú'
    VIDA_Y_LIBERTAD = 'Vida y Libertad'
    DIGNIDAD_Y_DEMOCRACIA = 'Dignidad y Democracia'

    BANCADAS = (
        (ACCION_POPULAR, 'Acción Popular'),
        (ALIANZA_PARA_EL_PROGRESO, 'Alianza para el Progreso'),
        (DEMOCRACIA_DIRECTA, 'Democracia Directa'),
        (DIGNIDAD_Y_DEMOCRACIA, 'Dignidad y Democracia'),
        (EL_FRENTE_AMPLIO_POR_JUSTICIA, 'El Frente Amplio por Justicia'),
        (FUERZA_POPULAR, 'Fuerza Popular'),
        (PARTIDO_APRISTA_PERUANO, 'Partido Aprista Peruano'),
        (PARTIDO_DEMOCRATICO_SOMOS_PERU, 'Partido Democrático Somos Perú'),
        (PARTIDO_HUMANISTA_PERUANO, 'Partido Humanista Peruano'),
        (PARTIDO_NACIONALISTA_PERUANO, 'Partido Nacionalista Peruano'),
        (PARTIDO_POLITICO_ORDEN, 'Partido Político Orden'),
        (PARTIDO_POPULAR_CRISTIANO, 'Partido Popular Cristiano-PPC'),
        (PERU_MAS, 'Perú Más'),
        (PERU_PATRIA_SEGURA, 'Perú Patria Segura'),
        (PERU_POSIBLE, 'Perú Posible'),
        (PERU_POSIBLE, 'Perú Posible'),
        (RESTAURACION_NACIONAL, 'Restauración Nacional'),
        (SIEMPRE_UNIDOS, 'Siempre Unidos'),
        (SOLIDARIDAD_NACIONAL, 'Solidaridad Nacional'),
        (TIERRA_Y_LIBERTAD, 'Tierra y Libertad'),
        (TODOS_POR_EL_PERU, 'Todos por el Perú'),
        (UNION_POR_EL_PERU, 'Unión por el Perú'),
        (VAMOS_PERU, 'Vamos Perú'),
        (VIDA_Y_LIBERTAD, 'Vida y Libertad'),
    )

    BANCADA = models.CharField(
        max_length=128,
        choices=BANCADAS
    )

    PAGINA_WEB = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    PAGINA_WEB2 = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    EMAIL_1 = models.EmailField(
        max_length=512,
        null=True,
        blank=True
    )

    EMAIL_2 = models.EmailField(
        max_length=512,
        null=True,
        blank=True
    )

    EMAIL_3 = models.EmailField(
        max_length=512,
        null=True,
        blank=True
    )

    DIRECCION_LIMA = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    DISTRITO_LIMA = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    PROVINCIA_LIMA = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    DIRECCION_REGION = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    DISTRITO_REGION = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    PROVINCIA_REGION = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    TELEFONO_LIMA_1 = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    TELEFONO_LIMA_2 = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    TELEFONO_CELULAR = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    TELEFONO_REGION_1 = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    TELEFONO_REGION_2 = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    TELEFONO_REGION_3 = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    TWITTER = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    FACEBOOK = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    GOOGLEP = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    YOUTUBE = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    BLOG = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    FLICKR = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    ISSUU = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    IBLUPS = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    OTROS = models.URLField(
        max_length=512,
        null=True,
        blank=True
    )

    PROYECTO_LEY = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Congresita"
        verbose_name_plural = "Congresitas"

        db_table = TABLES['Congresman']

        ordering = ('NOMBRE','APELLIDOS')

    def __str__(self):
        return '{0} {1}, {2} por la región {3}'.format(
            self.NOMBRE,
            self.APELLIDOS,
            self.CARGO,
            self.REGION
        )

    def getData(self):
        return dict({
            'NOMBRE': self.NOMBRE,
            'APELLIDOS': self.APELLIDOS,
            'CARGO': self.CARGO,
            'REGION': self.REGION,
            'BANCADA': self.BANCADA,
            'PAGINA_WEB': self.PAGINA_WEB,
            'PAGINA_WEB2': self.PAGINA_WEB2,
            'EMAIL_1': self.EMAIL_1,
            'EMAIL_2': self.EMAIL_2,
            'EMAIL_3': self.EMAIL_3,
            'DIRECCION_LIMA': self.DIRECCION_LIMA,
            'DISTRITO_LIMA': self.DISTRITO_LIMA,
            'PROVINCIA_LIMA': self.PROVINCIA_LIMA,
            'DIRECCION_REGION': self.DIRECCION_REGION,
            'DISTRITO_REGION': self.DISTRITO_REGION,
            'PROVINCIA_REGION': self.PROVINCIA_REGION,
            'TELEFONO_LIMA_1': self.TELEFONO_LIMA_1,
            'TELEFONO_LIMA_2': self.TELEFONO_LIMA_2,
            'TELEFONO_CELULAR': self.TELEFONO_CELULAR,
            'TELEFONO_REGION_1': self.TELEFONO_REGION_1,
            'TELEFONO_REGION_2': self.TELEFONO_REGION_2,
            'TELEFONO_REGION_3': self.TELEFONO_REGION_3,
            'TWITTER': self.TWITTER,
            'FACEBOOK': self.FACEBOOK,
            'GOOGLEP': self.GOOGLEP,
            'YOUTUBE': self.YOUTUBE,
            'BLOG': self.BLOG,
            'FLICKR': self.FLICKR,
            'ISSUU': self.ISSUU,
            'IBLUPS': self.IBLUPS,
            'OTROS': self.OTROS,
            'PROYECTO_LEY': self.PROYECTO_LEY,
        })
