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

@login_required(login_url='/login/')
def zanyatie (request, item_id=1) :
	user = request.user.username
	name_user 		 = Zanyatie.objects.get(id=item_id)
	yprazneniya_list = Yprazneniya.objects.filter(zanyatie=item_id)
	zanyatie_list	 = Podhod.objects.filter(zanyatie=item_id)

	vid_treni_list = Vid_Treni.objects.all()
	vid_podhoda_list = Vid_Podhod.objects.all()
	pp_yprazneniya_list = PP_Yprazneniya.objects.all()

	return render_to_response ('zanyatie.html', locals() , context_instance=RequestContext(request))



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
	return render_to_response ('add_zanyatie_new.html', locals() , context_instance=RequestContext(request))	


@login_required(login_url='/login/')
def add_ypraznenie (request) :
	user = request.user.username
	if request.method == "POST":
		zanyatie = request.POST['zanyatie']
		pp       = request.POST.get('pp')
		tip      = request.POST.get('tip')
		vid      = request.POST.get('vid')


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
	return render_to_response ('add_ypraznenie.html', locals() , context_instance=RequestContext(request))



#def save_zanyatie (request) :
#	user = request.user.username
#	zanyatie = request.GET['zanyatie']
#	ypraznenie = request.GET['ypraznenie']
#	tip = request.GET['tip']
#	vid = request.GET['vid']
#	podhod_00_ves = request.GET['podhod-1-ves']
#	podhod_00_raz = request.GET['podhod-1-raz']
#	podhod_0_ves = request.GET['podhod-0-ves']
#	podhod_0_raz = request.GET['podhod-0-raz']
#	podhod_1_ves = request.GET['podhod+1-ves']
#	podhod_1_raz = request.GET['podhod+1-raz']
#	podhod_2_ves = request.GET['podhod+2-ves']
#	podhod_2_raz = request.GET['podhod+2-raz']
#	podhod_3_ves = request.GET['podhod+3-ves']
#	podhod_3_raz = request.GET['podhod+3-raz']
#	podhod_4_ves = request.GET['podhod+4-ves']
#	podhod_4_raz = request.GET['podhod+4-raz']
#	podhod_5_ves = request.GET['podhod+5-ves']
#	podhod_5_raz = request.GET['podhod+5-raz']
#
#	z= Zanyatie.objects.get(id=zanyatie)
#	y= Yprazneniya.objects.get(id=ypraznenie)
	#pp = PP_Yprazneniya.objects.get(id=ypraznenie)
	#t= Vid_Treni.objects.get(id=ypraznenie)

#s	y= Yprazneniya.objects.get(id=ypraznenie)
#P_Podhod, PP_Yprazneniya, Vid_Podhod, Vid_Treni, Podhod, Zanyatie, Yprazneniya


#	p1=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya = u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'1' ,povtoreniya = podhod_00_raz, ves = podhod_00_ves)

##	p2=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'2' ,povtoreniya = podhod_0_raz, ves = podhod_0_ves)

#	p3=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'3' ,povtoreniya = podhod_1_raz, ves = podhod_1_ves)

#	p4=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'4' ,povtoreniya = podhod_2_raz, ves = podhod_2_ves)	
#
#	p5=Podhod( zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'5' ,povtoreniya = podhod_3_raz, ves = podhod_3_ves)
#
#	p6=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'6' ,povtoreniya = podhod_4_raz, ves = podhod_4_ves)
#
#	p7=Podhod(zanyatie = z, ypraznenie = y, pp_yprazneniya =  u'1', vid_treni = tip, 
#				vid_podhoda = vid, pp_podhoda =  u'7' ,povtoreniya = podhod_5_raz, ves = podhod_5_ves)									

#	podhodi_list = [p1,p2,p3,p4,p5,p6,p7]

	#vid_ypr.save()
#	return render_to_response('save_zanyatie.html', locals(), context_instance=RequestContext(request) )


def save_zanyatie_ypr (request) :
	user = request.user.username
	zan = request.POST['zanyatie']
	ypr = request.POST['ypraznenie']
	tip = request.POST['tip']
	vid = request.POST['vid']


	zanyatie= Zanyatie.objects.get(id=zan)
	ypraznenie= Yprazneniya.objects.get(id=ypr)


	try:
	    p1 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'0' )
	except Podhod.DoesNotExist:
	    p1 = None
	try:
	    p2 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'1' )
	except Podhod.DoesNotExist:
	    p2 = None
	try:
	    p3 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'2' )
	except Podhod.DoesNotExist:
	    p3 = None
	try:
	    p4 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'3' )
	except Podhod.DoesNotExist:
	    p4 = None
	try:
	    p5 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'4' )
	except Podhod.DoesNotExist:
	    p5 = None

	try:
	    p6 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'5' )
	except Podhod.DoesNotExist:
	    p6 = None

	try:
	    p7 = Podhod.objects.get(zanyatie=zanyatie, ypraznenie=ypraznenie, pp_podhoda= u'6' )
	except Podhod.DoesNotExist:
	    p7 = None

	podhodi_list = [p1,p2,p3,p4,p5,p6,p7]

	pp_ypr = ypraznenie.pp_yprazneniya.name

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


			podhod=Podhod(zanyatie = zanyatie, ypraznenie = ypraznenie, pp_yprazneniya = pp_ypr, vid_treni = tip, 
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
	return render_to_response('ypraznenie.html', locals(), context_instance=RequestContext(request) )




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


def login( request) :

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



