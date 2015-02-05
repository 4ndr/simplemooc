from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details')usando numero na url
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details')#usando slug na url
                    #\w para caracteres alfanumericos
                    #_ e - tambem aceita underline e hifen
                    #+ por que podem vir mais de uma vez
)