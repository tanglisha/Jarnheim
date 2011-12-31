from django.contrib import admin

# import all the models from the RPF
#from jarnheim.rpf.models import *
from Jarnheim.rpf.race import *
from Jarnheim.rpf.ban import *
from Jarnheim.rpf.character import *
from Jarnheim.rpf.guild import *

admin.site.register(race)
admin.site.register(ban)
admin.site.register(character)
admin.site.register(guild)
