from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response

#from django.contrib import auth
#from django.core.context_processors import csrf
#from forms import MyRegistrationForm

from trenirovka.models import PP_Podhod, PP_Yprazneniya, Vid_Podhod, Vid_Treni


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

