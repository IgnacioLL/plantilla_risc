from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	Fecha = forms.DateField(input_formats=['%d/%m/%Y'], label="Fecha (dd/mm/yyyy)")
	Fecha_cobro = forms.DateField(input_formats=['%d/%m/%Y'], label="Fecha cobro (dd/mm/yyyy)", required = False)
	Deadline_informe = forms.DateField(input_formats=['%d/%m/%Y'], label="Deadline Informe (dd/mm/yyyy)", required = False)
	Fecha_valoracion_retroactiva = forms.DateField(input_formats=['%d/%m/%Y'], label="Fecha valoracion retroactiva (dd/mm/yyyy)", required = False)

	class Meta:
		model = Contact
		exclude = ["timestamp", ]
		widgets = {
			'Descripcion': forms.Textarea(attrs={'rows':3, 'cols':15}),
			'Observaciones': forms.Textarea(attrs={'rows':4, 'cols':15}),

		}


	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
