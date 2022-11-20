from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Contact(models.Model):
	ESP = 'ESP'
	CAT = 'CAT'
	OTRO = 'OTRO'
	opciones = [(ESP, 'ESP'),(CAT, 'CAT'), (OTRO, 'OTRO'),]



	NAVE = 'NAVE'
	LOCAL = 'LOCAL'
	VIVIENDA = 'VIVIENDA'
	EDIFICIO = 'EDIFICIO'
	OFICINA = 'OFICINA'
	OTRO = 'OTRO'
	opciones_tipo_inmueble = [(NAVE, 'NAVE'),(LOCAL, 'LOCAL'), (VIVIENDA, 'VIVIENDA'),(EDIFICIO, 'EDIFICIO'),(OFICINA, 'OFICINA'),(OTRO, 'OTRO'),]

	Si = 'Si'
	No = 'No'
	opciones_valoracion_retroactiva = [(Si, 'Si'),(No, 'No'),]

	Cliente = "Cliente"
	Fecha = models.DateField()
	Idioma_Presupuesto = models.CharField(max_length = 3, choices = opciones, default = ESP)
	Idioma_Informe = models.CharField(max_length = 3, choices = opciones, default = ESP)
	Numero_de_Inmuebles = models.IntegerField()
	Tipo_Inmueble = models.CharField(max_length = 15, choices=opciones_tipo_inmueble, default=VIVIENDA)
	Descripcion = models.CharField(max_length= 300, blank=True)
	Encargado_por = models.CharField(max_length= 50, default = Cliente)
	Conocido_por = models.CharField(max_length=20)
	Objetivo_Valoracion = models.CharField(max_length=30)
	Tarifa = models.CharField(max_length= 30)
	Comision = models.FloatField("Comision (%)", validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
	Importe_presupuesto = models.FloatField()
	Importe_presupuesto_con_IVA = models.FloatField()
	Provision_inicial = models.FloatField("Provision Inicial (%)", validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
	Importe_Provision = models.FloatField()
	Provision_hecha = models.FloatField("Provision hecha (%)", validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
	Fecha_cobro = models.DateField(blank=True, null=True)
	Deadline_informe = models.DateField(blank=True, null=True)
	Valoracion_retroactiva = models.CharField(max_length = 2, choices = opciones_valoracion_retroactiva, default = No)
	Fecha_valoracion_retroactiva = models.DateField(blank=True, null=True)
	Observaciones = models.CharField(max_length=500, blank=True, null=True)

	
	timestamp = models.DateTimeField(default=datetime.datetime.now(pytz.timezone('Europe/Berlin')))

	def __str__(self):
		return self.name