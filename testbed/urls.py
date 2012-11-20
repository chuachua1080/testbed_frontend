from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^login$',  'auth.login'),
    (r'^logout$',  'auth.logout'),
    (r'^$','main.index'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
    # Examples:
    # url(r'^$', 'testbed.views.home', name='home'),
    # url(r'^testbed/', include('testbed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^pro$','pro.index'),
    (r'^pro/create$','pro.create'),
    (r'^pro/create_db$','pro.create_db'),
    (r'^pro/(?P<pro_id>\d+)/info$','pro.info'),
    (r'^pro/(?P<pro_id>\d+)/edit$','pro.edit'),
    (r'^pro/(?P<pro_id>\d+)/edit_db$','pro.edit_db'),
    (r'^pro/(?P<pro_id>\d+)/remove$','pro.remove'),
    (r'^(?P<pro_id>\d+)/top/create$','top.create'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/show$','top.show'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/edit$','top.edit'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/remove$','top.remove'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/export$','top.export'),
    (r'^ajax/top/(?P<top_id>\d+)/device_create$','ajax.device_create'),
    (r'^ajax/top/(?P<top_id>\d+)/device_load$','ajax.device_load'),
    (r'^ajax/top/(?P<dev_id>\d+)/device_remove$','ajax.device_remove'),
    (r'^ajax/top/(?P<top_id>\d+)/ovs_create$','ajax.ovs_create'),
    (r'^ajax/top/(?P<dev_id>\d+)/ovs_remove$','ajax.ovs_remove'),
    (r'^ajax/top/(?P<top_id>\d+)/top_tab$','ajax.top_tab'),
    (r'^ajax/top/(?P<top_id>\d+)/top_mod$','ajax.top_mod'),	
    (r'^ajax/top/(?P<dev_id>\d+)/ovs_tab$','ajax.ovs_tab'),	
    (r'^ajax/top/(?P<dev_id>\d+)/ovs_mod$','ajax.ovs_mod'),	
    (r'^ajax/top/(?P<dev_id>\d+)/host_tab$','ajax.host_tab'),
    (r'^ajax/top/(?P<dev_id>\d+)/host_mod$','ajax.host_mod'),	
    (r'^ajax/top/(?P<top_id>\d+)/con_create','ajax.con_create'),
    (r'^ajax/top/(?P<top_id>\d+)/con_remove','ajax.con_remove'),
    (r'^ajax/top/con_tab$','ajax.con_tab'),	
    (r'^ajax/(?P<s_id>.+)/(?P<t_id>.+)/con_mod$','ajax.con_mod'),
    (r'^ajax/top/(?P<top_id>\d+)/run','ajax.run'),
)
