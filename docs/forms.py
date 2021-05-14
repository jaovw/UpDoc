from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Selecione um documento para upload',
        help_text='Máximo 42 Megabytes'
    )