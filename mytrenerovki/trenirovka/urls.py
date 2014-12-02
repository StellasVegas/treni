from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytrenerovki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^podhodi/$', 'trenirovka.views.pp_podhod'),
    url(r'^ypr/$', 'trenirovka.views.pp_yprazneniya'),
    url(r'^ypraznenie/get/(?P<ypraznenie_id>\d+)/$', 'trenirovka.views.ypraznenie'),
    url(r'^vid_podhoda/$', 'trenirovka.views.vid_podhoda'),
    url(r'^vid_treni/$', 'trenirovka.views.vid_treni'),
    url(r'^add_vid_ypr/$', 'trenirovka.views.add_vid_ypr'),
    url(r'^add_vid_ypr/save_vid_ypr/$', 'trenirovka.views.save_vid_ypr'),
    url(r'^vse_podhodi/$', 'trenirovka.views.vse_podhodi'),
    url(r'^zanyatiya/get/(?P<item_id>\d+)/$', 'trenirovka.views.zanyatie'),
    url(r'^zanyatiya/$', 'trenirovka.views.vse_zanyatiya'),
    url(r'^ypraznenie/save_zanyatie_ypr/$', 'trenirovka.views.save_zanyatie_ypr'),
    url(r'^add_zanyatie/save_zanyatie/$', 'trenirovka.views.save_zanyatie'),
    url(r'^add_zanyatie/$', 'trenirovka.views.add_zanyatie'),
    url(r'^add_ypraznenie/$', 'trenirovka.views.add_ypraznenie'),
    url(r'^login/$', 'trenirovka.views.login'),
    url(r'^$', 'trenirovka.views.pp_podhod'),
)

