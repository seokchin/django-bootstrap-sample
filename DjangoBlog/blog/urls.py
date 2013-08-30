from django.conf.urls import patterns, include, url
from blog import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBlog.views.home', name='home'),
    # url(r'^DjangoBlog/', include('DjangoBlog.foo.urls')),
    url(r'list', views.IndexView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'create', views.CreateView.as_view(), name='create'),
    url(r'update/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.DeleteView.as_view(), name='delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
