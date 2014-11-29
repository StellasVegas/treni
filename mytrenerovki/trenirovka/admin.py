from django.contrib import admin

# Register your models here.

from trenirovka.models import PP_Podhod, PP_Yprazneniya, Vid_Podhod, Vid_Treni, Podhod, Zanyatie, Yprazneniya

# Register your models here.
admin.site.register(PP_Podhod)

admin.site.register(PP_Yprazneniya)

admin.site.register(Vid_Podhod)

admin.site.register(Vid_Treni)

admin.site.register(Podhod)

admin.site.register(Zanyatie)

admin.site.register(Yprazneniya)


