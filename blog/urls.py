from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	   (r'^add/$', 'blog.article.views.add'),


       (r'^comment/add/$', 'blog.article.views.comment_add'),

	   
	   (r'^list/$', 'blog.article.views.list'),

       (r'^view/(?P<id>[\d]+)$', 'blog.article.views.view'),

    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
