from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)

'''
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class Eshopping(AdminSite):
    site_title =ugettext_lazy('Django Admin site')

    site_header = ugettext_lazy('Django adminis')

    index_title = ugettext_lazy('Site Admin')

mydamin = Eshopping()'''




