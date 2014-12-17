from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytrenerovki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^podhodi/$', 'trenirovka.views.pp_podhod'),
    url(r'^ypr/$', 'trenirovka.views.pp_yprazneniya'),
    url(r'^ypraznenie/get/(?P<ypraznenie_id>\d+)/$', 'trenirovka.views.ypraznenie', name='ypr'),
    url(r'^vid_podhoda/$', 'trenirovka.views.vid_podhoda'),
    url(r'^vid_treni/$', 'trenirovka.views.vid_treni'),
    url(r'^add_vid_ypr/$', 'trenirovka.views.add_vid_ypr'),
    url(r'^add_vid_ypr/save_vid_ypr/$', 'trenirovka.views.save_vid_ypr'),
    url(r'^vse_podhodi/$', 'trenirovka.views.vse_podhodi'),
    url(r'^zanyatiya/get/(?P<item_id>\d+)/$', 'trenirovka.views.zanyatie', name='zan'),
    url(r'^zanyatiya/change_date/$', 'trenirovka.views.change_date'),
    url(r'^zanyatie/recover/(?P<zanyatie_id>\d+)$', 'trenirovka.views.zanyatie_recover'),
    url(r'^zanyatie/delete/(?P<zanyatie_id>\d+)$', 'trenirovka.views.zanyatie_delete'),
    url(r'^zanyatiya/$', 'trenirovka.views.vse_zanyatiya'),
    url(r'^yprazneniya/$', 'trenirovka.views.vse_yprazneniya'),
    url(r'^ypraznenie/save_zanyatie_ypr/$', 'trenirovka.views.save_zanyatie_ypr'),
 #   url(r'^add_zanyatie/save_zanyatie/$', 'trenirovka.views.save_zanyatie'),
    url(r'^add_zanyatie/$', 'trenirovka.views.add_zanyatie'),
    url(r'^add_ypraznenie_delete/(?P<ypraznenie_id>\d+)$', 'trenirovka.views.add_ypraznenie_delete'),
    url(r'^add_ypraznenie/$', 'trenirovka.views.add_ypraznenie'),
    url(r'^login/$', 'trenirovka.views.user_login', name='auth_login'),
    url(r'^register/$', 'trenirovka.views.register', name='register'),
    url(r'^logout/$', 'trenirovka.views.user_logout', name='logout'),
    url(r'^$', 'trenirovka.views.home'),
)

