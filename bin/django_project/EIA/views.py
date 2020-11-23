from django.shortcuts import render
from EIA.models import showid
from EIA.forms import QueryForm

def EIAhome(request):
	return render(request, 'EIA/EIAhome.html')

def EIAquery(request):
	results = showid.objects.all()
	anotherresult = results.values_list('eiaplantid', flat=True).distinct()
	unitresults = results.values_list('unit', flat=True).distinct()
	plantnameresults = results.values_list('eiaplantname', flat=True).distinct()
	statusresults = results.values_list('status', flat=True).distinct()
	mwcapacityresults = results.values_list('mwcapacity', flat=True).distinct()
	latituderesults = results.values_list('latitude', flat=True).distinct()
	noresultsflag = False

	if (request.method == "POST"):
		selectedplantid = request.POST['eiaplantidselect']
		selectedunit = request.POST['eiaunitselect']
		selectedplantname = request.POST['eiaplantnameselect']
		selectedstatus = request.POST['eiastatusselect']
		selectedmwcapacity = request.POST['eiamwcapacityselect']
		selectedlatitude = request.POST['eialatitudeselect']

		parameterdict = {}
		if (selectedplantid != "---------"):
			parameterdict['eiaplantid'] = selectedplantid
		if (selectedunit != "---------"):
			parameterdict['unit'] = selectedunit
		if (selectedplantname != "---------"):
			parameterdict['eiaplantname'] = selectedplantname
		if (selectedstatus != "---------"):
			parameterdict['status'] = selectedstatus
		if (selectedmwcapacity != "---------"):
			parameterdict['mwcapacity'] = selectedmwcapacity
		if (selectedlatitude != "---------"):
			parameterdict['latitude'] = selectedlatitude

		isparameterdictempty = not parameterdict
		if (isparameterdictempty == False):
			queryresults = results.filter(**parameterdict).order_by('eiaplantname').values_list('eiaplantid', 'unit', 'eiaplantname', 'status', 'mwcapacity', 'latitude')
			if (len(queryresults) < 1):
				noresultsflag = True
				returnedrecordnumber = "Returned Record(s) Number: 0"
			else:
				returnedrecordnumber = "Returned Record(s) Number: " + str(len(queryresults))
		else:
			queryresults = results.order_by('eiaplantname').values_list('eiaplantid', 'unit', 'eiaplantname', 'status', 'mwcapacity', 'latitude')
			returnedrecordnumber = "Returned Record(s) Number: " + str(len(queryresults))
			'''print (queryresults)'''
		print(selectedplantid + " | " + selectedunit + " | " + selectedplantname + " | " + selectedstatus + " | " + selectedmwcapacity + " | " + selectedlatitude)
		'''.objects.filter(which_photo=which_photo).order_by('-id').values_list('submitted_by', flat=True)[:25]'''
		'''MyQueryForm = QueryForm(request.POST)

		if MyQueryForm.is_valid():
			selectedplantid = MyQueryForm.cleaned_data['eiaplantidselect']
			selectedunit = MyQueryForm.cleaned_data['eiaunitselect']
			selectedplantname = MyQueryForm.cleaned_data['eiaplantnameselect']

			print ("Getting Here?")

			return render(request, 'EIA/EIAquery.html', {"showid":results, "showanother":anotherresult, "showunit":unitresults, "showplantname":plantnameresults, "showselectedplantid":selectedplantid, "showselectedunit":selectedunit, "showselectedplantname":selectedplantname})

		else:
			selectedplantid = "No selection made"
			selectedunit = "No selection made"
			selectedplantname = "No selection made"

			print (MyQueryForm.errors)'''

		return render(request, 'EIA/EIAquery.html', {"showid":results, "showanother":anotherresult, "showunit":unitresults, "showplantname":plantnameresults, "showstatus":statusresults, "returnedqueryresults":queryresults, "shownoresultsflag":noresultsflag, "showreturnedrecordnumber":returnedrecordnumber, "showmwcapacity":mwcapacityresults, "showlatitude":latituderesults})

	else:
		'''MyQueryForm = QueryForm()
		selectedplantid = "No selection made"
		selectedunit = "No selection made"
		selectedplantname = "No selection made"'''

		queryresults = results.order_by('eiaplantname').values_list('eiaplantid', 'unit', 'eiaplantname', 'status', 'mwcapacity', 'latitude')
		returnedrecordnumber = "Returned Record(s) Number: " + str(len(queryresults))
		'''for x in results:
		addflag = True
		for v in subset:
			if (results[x] == subset[v]):
				addflag = False
				break
		if (addflag == True):
			subset.append(results[x])'''
		return render(request, 'EIA/EIAquery.html', {"showid":results, "showanother":anotherresult, "showunit":unitresults, "showplantname":plantnameresults, "showstatus":statusresults, "returnedqueryresults":queryresults, "shownoresultsflag":noresultsflag, "showreturnedrecordnumber":returnedrecordnumber, "showmwcapacity":mwcapacityresults, "showlatitude":latituderesults})
'''def EIAqueryresults(request):
	if request.method == "POST":
    	MyQueryForm = QueryForm(request.POST)
      
    	if MyQueryForm.is_valid():
    		selectedplantid = MyQueryForm.cleaned_data['eiaplantidselect']
    		selectedunit = MyQueryForm.cleaned_data['eiaunitselect']
    		selectedplantname = MyQueryForm.cleaned_data['eiaplantnameselect']

	else:
		MyQueryForm = QueryForm()
		
	return render(request, '', {"username" : username})'''