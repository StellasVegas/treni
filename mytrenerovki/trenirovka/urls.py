from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytrenerovki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^podhodi/$', 'trenirovka.views.pp_podhod'),
    url(r'^ypr/$', 'trenirovka.views.pp_yprazneniya'),
    url(r'^vid_podhoda/$', 'trenirovka.views.vid_podhoda'),
    url(r'^vid_treni/$', 'trenirovka.views.vid_treni'),
    url(r'^$', 'trenirovka.views.pp_podhod'),
)
