from django.conf.urls.defaults import patterns, include, url
from registro.views import *

urlpatterns = patterns('',
   url(r'^$', 'registro.views.index', name='home'),
   url(r'^metodologia/$', 'registro.views.metodologia', name='metodologia'),
   url(r'^patrocinadores/$', 'registro.views.patrocinadores', name='patrocinadores'),   
   url(r'^preinscripcion$',NuevaInscripcion.as_view(), name='preinscripcion'),   
   url(r'^correcto$','registro.views.correcto', name='correcto'),   
   
)