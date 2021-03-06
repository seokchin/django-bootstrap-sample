from django.conf.urls import patterns, include, url
from blog.models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
admin.site.register(Post)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBlog.views.home', name='home'),
    # url(r'^DjangoBlog/', include('DjangoBlog.foo.urls')),
    url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
