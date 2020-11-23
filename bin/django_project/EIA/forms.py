from django import forms
from EIA.models import showid

class QueryForm(forms.Form):
	plantidchoices = showid.objects.values_list('eiaplantid', flat=True).distinct()
	unitchoices = showid.objects.values_list('unit', flat=True).distinct()
	plantnamechoices = showid.objects.values_list('eiaplantname', flat=True).distinct()
	statuschoices = showid.objects.values_list('status', flat=True).distinct()
	mwcapacitychoices = showid.objects.values_list('mwcapacity', flat=True).distinct()

	plantid = forms.ChoiceField(widget=forms.Select(choices=plantidchoices))
	unit = forms.ChoiceField(widget=forms.Select(choices=unitchoices))
	plantname = forms.ChoiceField(widget=forms.Select(choices=plantnamechoices))
	status = forms.ChoiceField(widget=forms.Select(choices=statuschoices))
	mwcapacity = forms.ChoiceField(widget=forms.Select(choices=mwcapacitychoices))