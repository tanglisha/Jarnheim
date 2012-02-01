from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.views.generic import list_detail
from characters.models import Character

character_info = {'queryset': Character.objects.all(),
                  'template_object_name': 'character'}

urlpatterns = patterns('characters.views',
                       url(r'^$', list_detail.object_list,
                           dict(character_info,
                                template_name='character_list.html')),
                       url(r'^(?P<slug>)\w/$',
                           dict(character_info,
                                slug_field="slug",
                                template_name='character_detail.html')),
                       url(r'^new/$', 'character_register'),)
