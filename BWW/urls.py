from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from .views import ArbeitskraftList
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'arbeitskraft',views.ArbeitskraftViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^$', views.home, name='home'),

   #Arbeitskraft for Web
    url(r'^ak_list/$', views.arbeitskraft_list, name='arbeitskraft_list'),
    url(r'^ak_detail/(?P<pk>\d+)/$', views.arbeitskraft_detail, name='arbeitskraft_detail'),
    url(r'^ak/new/$', views.arbeitskraft_neu, name='arbeitskraft_neu'),
    url(r'^ak/(?P<pk>\d+)/edit/$', views.arbeitskraft_edit, name='arbeitskraft_edit'),

    #Firma for Web
    url(r'^firma_list/$',views.firma_list, name='firma_list'),
    url(r'^firma_detail/(?P<pk>\d+)/$',views.firma_detail, name='firma_detail'),
    url(r'^firma/new/$', views.firma_neu, name='firma_neu'),
    url(r'^firma/(?P<pk>\d+)/edit/$', views.firma_edit, name='firma_edit'),


    #Arbeitskraft for REST

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^arbeitskraft/f/(?P<nachname>.+)/$', ArbeitskraftList.as_view()), # URL to filter REST request for arbeitskraft list by nachname
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)