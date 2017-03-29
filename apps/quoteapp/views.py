from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from . models import Users, Quotes, Favorites
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def index(request):
	user = request.session['log_user_id']
	context={
		'user':Users.objects.get(id = user),
		'quote': Quotes.objects.all().exclude(fav_quotes__user=user),
		'favs': Favorites.objects.filter(user = user).order_by('created_at')
	}
	print Favorites.objects.all()
	return render(request, 'quoteapp/index.html', context)

def create(request):
	if request.method == 'POST':
		user = request.session['log_user_id']
		if len(request.POST['creator']) <= 3:
			messages.error(request,'Name must be more than 3 characters.')
			return redirect(reverse('quote:index'))
		if len(request.POST['content']) <= 10:
			messages.error(request,'Message must be more than 10 characters.')
			return redirect(reverse('quote:index'))

		Quotes.objects.create(creator= request.POST['creator'],content=request.POST['content'], user = Users.objects.get(id = user))
	return redirect(reverse('quote:index'))

def fav(request,id):
	if request.method == 'POST':
		user = Users.objects.get(id = request.session['log_user_id'])
		quote = Quotes.objects.get(id = id)
		Favorites.objects.create(quote = quote, user = user)

	return redirect(reverse('quote:index'))

def delete(request,id):
	if request.method == 'POST':
		Favorites.objects.filter(id = id).delete()
	return redirect(reverse('quote:index'))


def info(request,id):

	context={
		'user':Users.objects.get(id = id),
		'quote':Quotes.objects.filter(user=id),
		'count':Users.objects.filter(id = id).annotate(num_quotes=Count('all_users'))

	}
	return render(request, 'quoteapp/users.html', context)

