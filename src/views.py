from django.shortcuts import render

# Create your views here.


def events(request):
	dictionary ={ 'one' : 1, 'two' : 2, 'three' : 3}
	return render(request, 'events.html',{'dictionary':dictionary})
