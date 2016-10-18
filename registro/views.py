from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from registro.forms import *

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def metodologia(request):
	return render_to_response('metodologia.html', context_instance=RequestContext(request))

def patrocinadores(request):
	return render_to_response('patrocinadores.html', context_instance=RequestContext(request))

def correcto(request):
	return render_to_response('correcto.html', context_instance=RequestContext(request))

class NuevaInscripcion(TemplateView):
	plantilla = 'nueva_cordada.html'
	def get(self, request):
		formulario = FormularioNuevaCordada()
		return render_to_response(self.plantilla, locals(), context_instance=RequestContext(request))
	def post(self, request):
		formulario = FormularioNuevaCordada(request.POST)
		if formulario.is_valid():
			print "hola"
			formulario.save()
			return render_to_response('correcto.html', context_instance=RequestContext(request))
		else:
			error = True 
			formulario = FormularioNuevaCordada()
			return render_to_response(self.plantilla, locals(), context_instance=RequestContext(request))
    
			
			