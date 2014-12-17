from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
#from django.contrib import auth
#from django.core.context_processors import csrf
#from forms import MyRegistrationForm
import datetime
#from datetime import datetime  
from django.core.urlresolvers import reverse

from trenirovka.models import PP_Podhod, PP_Yprazneniya, Vid_Podhod, Vid_Treni, Podhod, Zanyatie, Yprazneniya, UserProfile
from trenirovka.forms import UserForm, UserProfileForm, ChangeDateZan

def home (request) :
	vid_treni_list = Vid_Treni.objects.all().filter(status = True)

	vid_podhoda_list = Vid_Podhod.objects.all()

	try:
	    user 	     = User.objects.get(username = request.user.username)
	    polsovatel 	 = UserProfile.objects.get(user = user) 
	    vse_zanyatiya_list = Zanyatie.objects.all().filter(user= polsovatel, status = True).order_by('date')[:3]
	except UserProfile.DoesNotExist:
	    vse_zanyatiya_list = None



	return render_to_response ('home.html', locals() )

def pp_podhod (request) :
	pp_podhod_list = PP_Podhod.objects.all()
	return render_to_response ('pp_podhod.html', locals() )

def pp_yprazneniya (request) :
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()
	return render_to_response ('pp_yprazneniya.html', locals() )

def vid_podhoda (request) :
	vid_podhoda_list = Vid_Podhod.objects.all()
	return render_to_response ('vid_podhod.html', locals() )

def vid_treni (request) :
	
	vid_treni_list = Vid_Treni.objects.all()
	return render_to_response ('vid_treni.html', locals() )


def vse_podhodi (request) :
	vse_podhodi_list = Podhod.objects.all()
	return render_to_response ('vse_podhodi.html', locals() )

@login_required(login_url='/login/')
def vse_zanyatiya (request) :
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 
	vse_zanyatiya_list = Zanyatie.objects.all().filter(user= polsovatel, status = True) 
	vse_zanyatiya_archive = Zanyatie.objects.all().filter(user= polsovatel, status = False).order_by('date').reverse()[:3]

	return render_to_response ('vse_zanyatiya.html', locals() )

@login_required(login_url='/login/')
def vse_yprazneniya (request) :
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 

	vse_yprazneniya_list = Yprazneniya.objects.all().filter(user= polsovatel, status = True, zanyatie__status__exact = True).order_by('zanyatie__date')
	vse_yprazneniya_archive = Yprazneniya.objects.all().filter(user= polsovatel, zanyatie__status__exact = False).order_by('zanyatie__date').reverse()[:3]

	return render_to_response ('vse_yprazneniya.html', locals() )

@login_required(login_url='/login/')
def zanyatie (request, item_id=1) :
	user = request.user.username

	zanyatie 		 = Zanyatie.objects.get(id=item_id)
	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=item_id, status = True)
	zanyatie_list	 = Podhod.objects.filter(zanyatie=item_id)


	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()

	N_pp = len(yprazneniya_list)+1
	try:
	    next_pp = PP_Yprazneniya.objects.get(pp=N_pp)
	except PP_Yprazneniya.DoesNotExist:
	    next_pp = None


	change_date_form = ChangeDateZan()

	return render_to_response ('zanyatie.html', locals() , context_instance=RequestContext(request),)

@login_required(login_url='/login/')
def change_date (request) :
	
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 
	if request.method == "POST":
		zanyatie_id = request.POST.get('zanyatie_id')
		date       = request.POST.get('date')


#	now = datetime.datetime.now()


	z= Zanyatie.objects.get(id=zanyatie_id)
	new_date = datetime.datetime.strptime(date, '%d.%m.%Y')
	z.date = new_date
	z.save()



	redirect_url = reverse('zan', args=[z.id])

	return HttpResponseRedirect(redirect_url)


def add_vid_ypr (request) :
	vid_treni_list = Vid_Treni.objects.all()
	return render_to_response ('add_vid_ypr.html', locals() )

def save_vid_ypr (request) :
	new = request.GET['vid']
	vid_ypr = Vid_Treni(name = new)
	vid_ypr.save()
	return redirect('/vid_treni/', locals() )


#@login_required(login_url='/login/')
#def add_zanyatie_old (request) :
#	user = request.user.username
#	new_zanyatie = Zanyatie(user = user)
#	new_zanyatie.save()

#	vid_treni_list = Vid_Treni.objects.all()
#	vid_podhoda_list = Vid_Podhod.objects.all()
#	return render_to_response ('add_zanyatie.html', locals() )

@login_required(login_url='/login/')
def zanyatie_delete (request, zanyatie_id) :
	
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 


	zanyatie = Zanyatie.objects.get(id=zanyatie_id)

	zanyatie.status = False
	zanyatie.save()


	#redirect_url = reverse('zan', args=[zanyatie.id])

	return HttpResponseRedirect('/zanyatiya/')

@login_required(login_url='/login/')
def zanyatie_recover (request, zanyatie_id) :
	
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 


	zanyatie = Zanyatie.objects.get(id=zanyatie_id)

	zanyatie.status = True
	zanyatie.save()


	#redirect_url = reverse('zan', args=[zanyatie.id])

	return HttpResponseRedirect('/zanyatiya/')

@login_required(login_url='/login/')
def add_zanyatie (request) :
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 
	new_zanyatie = Zanyatie(user = polsovatel, status = False)

	new_zanyatie.save()

	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=new_zanyatie)

	N_pp = len(yprazneniya_list)+1
	try:
	    next_pp = PP_Yprazneniya.objects.get(pp=N_pp)
	except PP_Yprazneniya.DoesNotExist:
	    next_pp = None

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()

	now = datetime.datetime.now()
	time = now.date()

	redirect_url = reverse('zan', args=[new_zanyatie.id])

	return HttpResponseRedirect(redirect_url)

#	return render_to_response ('add_zanyatie_new.html', locals() , context_instance=RequestContext(request))	


@login_required(login_url='/login/')
def add_ypraznenie (request) :
	
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 
	if request.method == "POST":
		zanyatie = request.POST['zanyatie']
		pp       = request.POST.get('pp')
		tip      = request.POST.get('tip')
		vid      = request.POST.get('vid')

	now = datetime.datetime.now()

	p= PP_Yprazneniya.objects.get(name=pp)
	t= Vid_Treni.objects.get(name=tip)
	v= Vid_Podhod.objects.get(name=vid )
	z= Zanyatie.objects.get(id=zanyatie)

	new_ypr = Yprazneniya(	user           = polsovatel,
							date     	   = now,
							pp_yprazneniya = p,
							vid_treni      = t,
							vid_podhoda    = v,
							zanyatie       = z)
	new_ypr.save()

	z.status = True
	z.save()


	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=zanyatie, status = True)

	N_pp = str(len(yprazneniya_list)+1)
	try:
	    next_pp = PP_Yprazneniya.objects.get(id=N_pp)
	except PP_Yprazneniya.DoesNotExist:
	    next_pp = None

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()


	redirect_url = reverse('zan', args=[z.id])

	return HttpResponseRedirect(redirect_url)

#	return render_to_response ('add_ypraznenie.html', locals() , context_instance=RequestContext(request))


@login_required(login_url='/login/')
def add_ypraznenie_delete (request, ypraznenie_id) :
	
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 

	ypraznenie = Yprazneniya.objects.get(id=ypraznenie_id)
	zanyatie = ypraznenie.zanyatie

	ypraznenie.status = False
	ypraznenie.save()


	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=zanyatie, status = True)

	N_pp = str(len(yprazneniya_list)+1)

	try:
	    next_pp = PP_Yprazneniya.objects.get(id=N_pp)
	except PP_Yprazneniya.DoesNotExist:
	    next_pp = None

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()

	redirect_url = reverse('zan', args=[zanyatie.id])

	return HttpResponseRedirect(redirect_url)

def save_zanyatie_ypr (request) :
	user 	     = User.objects.get(username = request.user.username)
	polsovatel 	 = UserProfile.objects.get(user = user) 

	zan = request.POST['zanyatie']
	ypr = request.POST['ypraznenie']
	tip = request.POST['tip']
	vid = request.POST['vid']


	zanyatie= Zanyatie.objects.get(id=zan)
	ypraznenie= Yprazneniya.objects.get(id=ypr)


	try:
	    p1 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'0' )
	except Podhod.DoesNotExist:
	    p1 = None
	try:
	    p2 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'1' )
	except Podhod.DoesNotExist:
	    p2 = None
	try:
	    p3 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'2' )
	except Podhod.DoesNotExist:
	    p3 = None
	try:
	    p4 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'3' )
	except Podhod.DoesNotExist:
	    p4 = None
	try:
	    p5 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'4' )
	except Podhod.DoesNotExist:
	    p5 = None

	try:
	    p6 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'5' )
	except Podhod.DoesNotExist:
	    p6 = None

	try:
	    p7 = Podhod.objects.get(user = polsovatel, zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'6' )
	except Podhod.DoesNotExist:
	    p7 = None

	podhodi_list = [p1,p2,p3,p4,p5,p6,p7]

	pp_ypr = ypraznenie.pp_yprazneniya.name

	now = datetime.datetime.now() 

	for num, podhod in enumerate(podhodi_list):
		if podhod is None:

			ves = 'podhod-%s-ves' % str(num)
			pod = 'podhod-%s-raz' % str(num)
			podhod_ves = request.POST.get(ves) 
			podhod_raz = request.POST.get(pod)

			povtoreniya = podhod_raz
			ves         = podhod_ves

#			podhod=Podhod(zanyatie = zanyatie, ypraznenie = ypraznenie, pp_yprazneniya = u'1', vid_treni = tip, 
#							vid_podhoda = vid, pp_podhoda =  num ,povtoreniya = povtoreniya, ves = ves)


			podhod=Podhod(user = polsovatel, zanyatie = zanyatie, date = now, ypraznenie = ypraznenie, pp_yprazneniya = pp_ypr, vid_treni = tip, 
							vid_podhoda = vid, pp_podhoda =  num )
			if ves :
				podhod.ves = ves 
			
			if povtoreniya:
				podhod.povtoreniya = povtoreniya 
			
			podhod.save()
			podhodi_list[num] = podhod

		else:
			ves = 'podhod-%s-ves' % str(num)
			pod = 'podhod-%s-raz' % str(num)
			podhod_ves = request.POST.get(ves) 
			podhod_raz = request.POST.get(pod) 
			if podhod_ves :
				podhod.ves         = int(podhod_ves)
			if podhod_raz :
				podhod.povtoreniya = int(podhod_raz)
			podhod.save()
			podhodi_list[num] = podhod


	#podhodi_list = [p1,p2,p3,p4,p5,p6,p7]


	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()

	#vid_ypr.save()

	redirect_url = reverse('ypr', args=[ypraznenie.id])

	return HttpResponseRedirect(redirect_url)

	#return render_to_response('ypraznenie.html', locals(), context_instance=RequestContext(request) )




@login_required(login_url='/login/')
def ypraznenie (request, ypraznenie_id) :
	user = request.user.username

	ypraznenie = Yprazneniya.objects.get(id=ypraznenie_id)
	zanyatie = ypraznenie.zanyatie
	#podhodi_list = Podhod.objects.filter (ypraznenie = ypraznenie)

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()

	try:
	    p1 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '0')
	except Podhod.DoesNotExist:
	    p1 = None
	    
	try:
	    p2 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '1')
	except Podhod.DoesNotExist:
	    p2 = None
	    
	try:
	    p3 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '2')
	except Podhod.DoesNotExist:
	    p3 = None
	    
	try:
	    p4 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '3')
	except Podhod.DoesNotExist:
	    p4 = None
	    
	try:
	    p5 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '4')
	except Podhod.DoesNotExist:
	    p5 = None
	    
	try:
	    p6 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '5')
	except Podhod.DoesNotExist:
	    p6 = None
	    
	try:
	    p7 = Podhod.objects.get(ypraznenie = ypraznenie, pp_podhoda  = '6')
	except Podhod.DoesNotExist:
	    p7 = None

	

	param = 1

	return render_to_response ('ypraznenie_create.html', locals() , context_instance=RequestContext(request))	

#old
def login_old( request) :

	#c = {}
   # c.update(csrf(request))
	if request.method == "POST":
		z = request.POST['zanyatie']

	if not request.user.is_authenticated():
		try :
			login 	 = request.POST['login']
			password = request.POST['password']
			user = auth.authenticate(username=login, password=password)
			if user and user.is_active:
				auth.login( request, user)
			else :
				return render_to_response('login.html', locals(), context_instance=RequestContext(request))
		except KeyError : 
			pass

	return render_to_response('login.html', locals(), context_instance=RequestContext(request))



def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')