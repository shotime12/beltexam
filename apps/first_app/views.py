from django.shortcuts import render, redirect
from ..loginapp.models import User
from .models import Destination
# Create your views here.
def index(request):
	user = User.objects.get(id=request.session['logged_in_user'])

	destinations = Destination.objects.filter(users=user)

	other_destinations = Destination.objects.exclude(users=user)
	


	context = {
		'user': user,
		'destinations': destinations,
		'other_destinations': other_destinations
	}
	return render(request, 'first_app/index.html', context)
def addPage(request):
	return render(request, 'first_app/createTrip.html')
	
def addTrip(request):
	print request.POST['start_date']
	print request.POST['end_date']
	if request.POST['start_date']>request.POST['end_date']:
		print 'IT WORKS!'
	if request.POST['start_date']>request.POST['end_date']:
		print 'This also works!!'


	did_create =  Destination.objects.addTrip(request)
	if did_create:
		user = User.objects.get(id=request.session['logged_in_user'])
		print '*' * 50
		print user
		print '*' * 50
		new_trip = Destination.objects.create(
		name = request.POST['name'],
		plan = request.POST['description'],
		start_date =  request.POST['start_date'],
		end_date = request.POST['end_date'],
		creator_user = user,
		)
		new_trip.users.add(user)
		new_trip.save()
	 	return redirect('/dashboard')
	else:
	 	return redirect('/dashboard/add')

	return redirect('/')

def join(request, id):
	user = User.objects.get(id=request.session['logged_in_user'])
	destination = Destination.objects.get(id=id)

	user.destinations.add(destination)
	user.save()
	return redirect('/dashboard')

def destination(request, id):
	destination = Destination.objects.get(id=id)
	
	users = User.objects.all()
	x= destination.users.all()
	print x.values()
	
	context = {
		'destination': destination,
		'x': x
	}
	
	return render(request, 'first_app/destinations.html', context)

def logout(request):
	del request.session['logged_in_user']
	return redirect('/')
