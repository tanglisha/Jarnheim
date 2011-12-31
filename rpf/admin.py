from django.contrib import admin

# import all the models from the RPF
from Jarnheim.rpf.models import *

admin.site.register(race)
admin.site.register(ban)
admin.site.register(character)
admin.site.register(guild)
