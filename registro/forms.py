from django.forms import DateInput
from django.forms import ModelForm
from django.forms import Select
from django.forms import BooleanField
from django.forms import Textarea
from django.forms import TextInput
from registro.models import Cordada

class FormularioNuevaCordada(ModelForm):
	class Meta:
		model = Cordada
		fields = ['nombre_cordada','escalador_uno','escalador_dos','categoria','numero_contacto']
		widgets = {			
			'nombre_cordada':TextInput(attrs={'required':'true'}),
			'escalador_uno':TextInput(attrs={'required':'true'}),
			'escalador_dos':TextInput(attrs={'required':'true'}),
			'categoria':Select(),
			'numero_contacto':TextInput(attrs={'required':'true'}),
		}

