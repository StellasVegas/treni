from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytrenerovki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('trenirovka.urls')),
)
