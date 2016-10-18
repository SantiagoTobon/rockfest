from django.db import models

# Create your models here.
CATEGORIA = ((1,"Femenino Experto"),(2,"Femenino Novato"),(3,"Masculino Experto"),(4,"Masculino Novato"),(5,"Mixta"))
 
class Cordada(models.Model):
	nombre_cordada = models.CharField(max_length=100)
	escalador_uno = models.CharField(max_length=100)
	escalador_dos = models.CharField(max_length=100)
	categoria = models.SmallIntegerField(choices=CATEGORIA)
	numero_contacto =  models.CharField(max_length=140)
	
	def __unicode__(self):
		return self.nombre_cordada

