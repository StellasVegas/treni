from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
#from django.contrib import auth
#from django.core.context_processors import csrf
#from forms import MyRegistrationForm

from trenirovka.models import PP_Podhod, PP_Yprazneniya, Vid_Podhod, Vid_Treni, Podhod, Zanyatie, Yprazneniya


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

def vse_zanyatiya (request) :
	vse_zanyatiya_list = Zanyatie.objects.all()
	return render_to_response ('vse_zanyatiya.html', locals() )

def zanyatie (request, item_id=1) :
	name_user 		 = Zanyatie.objects.get(id=item_id)
	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=item_id)
	zanyatie_list	 = Podhod.objects.filter(zanyatie=item_id)
	return render_to_response ('zanyatie.html', locals() )


def add_vid_ypr (request) :
	vid_treni_list = Vid_Treni.objects.all()
	return render_to_response ('add_vid_ypr.html', locals() )

def save_vid_ypr (request) :
	new = request.GET['vid']
	vid_ypr = Vid_Treni(name = new)
	vid_ypr.save()
	return redirect('/vid_treni/', locals() )


@login_required(login_url='/login/')
def add_zanyatie_old (request) :
	user = request.user.username
	new_zanyatie = Zanyatie(user = user)
	new_zanyatie.save()

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	return render_to_response ('add_zanyatie.html', locals() )



@login_required(login_url='/login/')
def add_zanyatie (request) :
	user = request.user.username
	new_zanyatie = Zanyatie(user = user)
	new_zanyatie.save()

	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=new_zanyatie)

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()
	return render_to_response ('add_zanyatie_new.html', locals() )	


@login_required(login_url='/login/')
def add_ypraznenie (request) :
	user = request.user.username
	zanyatie = request.GET['zanyatie']

	pp       = request.GET['pp']
	tip      = request.GET['tip']
	vid      = request.GET['vid']

	p= PP_Yprazneniya.objects.get(name=pp)
	t= Vid_Treni.objects.get(name=tip)
	v= Vid_Podhod.objects.get(name=vid )
	z= Zanyatie.objects.get(id=zanyatie)

	new_ypr = Yprazneniya(	pp_yprazneniya = p,
							vid_treni      = t,
							vid_podhoda    = v,
							zanyatie       = z )
	new_ypr.save()

	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=zanyatie)

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()
	return render_to_response ('add_ypraznenie.html', locals() )



def save_zanyatie (request) :
	user = request.user.username
	zanyatie = request.GET['zanyatie']
	ypraznenie = request.GET['ypraznenie']
	tip = request.GET['tip']
	vid = request.GET['vid']
	podhod_00_ves = request.GET['podhod-1-ves']
	podhod_00_raz = request.GET['podhod-1-raz']
	podhod_0_ves = request.GET['podhod-0-ves']
	podhod_0_raz = request.GET['podhod-0-raz']
	podhod_1_ves = request.GET['podhod+1-ves']
	podhod_1_raz = request.GET['podhod+1-raz']
	podhod_2_ves = request.GET['podhod+2-ves']
	podhod_2_raz = request.GET['podhod+2-raz']
	podhod_3_ves = request.GET['podhod+3-ves']
	podhod_3_raz = request.GET['podhod+3-raz']
	podhod_4_ves = request.GET['podhod+4-ves']
	podhod_4_raz = request.GET['podhod+4-raz']
	podhod_5_ves = request.GET['podhod+5-ves']
	podhod_5_raz = request.GET['podhod+5-raz']

	z= Zanyatie.objects.get(id=zanyatie)
	y= Yprazneniya.objects.get(id=ypraznenie)
	#pp = PP_Yprazneniya.objects.get(id=ypraznenie)
	#t= Vid_Treni.objects.get(id=ypraznenie)

#s	y= Yprazneniya.objects.get(id=ypraznenie)
#P_Podhod, PP_Yprazneniya, Vid_Podhod, Vid_Treni, Podhod, Zanyatie, Yprazneniya


	p1=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya = u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'1' ,povtoreniya = podhod_00_raz, ves = podhod_00_ves)

	p2=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'2' ,povtoreniya = podhod_0_raz, ves = podhod_0_ves)

	p3=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'3' ,povtoreniya = podhod_1_raz, ves = podhod_1_ves)

	p4=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'4' ,povtoreniya = podhod_2_raz, ves = podhod_2_ves)	

	p5=Podhod( zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'5' ,povtoreniya = podhod_3_raz, ves = podhod_3_ves)

	p6=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'6' ,povtoreniya = podhod_4_raz, ves = podhod_4_ves)

	p7=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
				vid_podhoda = vid, pp_podhoda =  u'7' ,povtoreniya = podhod_5_raz, ves = podhod_5_ves)									

	podhodi_list = [p1,p2,p3,p4,p5,p6,p7]

	#vid_ypr.save()
	return render_to_response('save_zanyatie.html', locals() )


def login( request) :

	#c = {}
   # c.update(csrf(request))

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



