from django.conf.urls import url

from submission import views

urlpatterns = [

    url(r'^start/$', views.start, name='submission_start'),
    url(r'^(?P<type>[-\w.]+)/start/$', views.start, name='submission_start'),
    url(r'^(?P<article_id>\d+)/info/$', views.submit_info, name='submit_info'),
    url(r'^(?P<article_id>\d+)/authors/$', views.submit_authors, name='submit_authors'),
    url(r'^(?P<article_id>\d+)/authors/(?P<author_id>\d+)/delete/$', views.delete_author, name='delete_author'),
    url(r'^(?P<article_id>\d+)/funders/(?P<funder_id>\d+)/delete/$', views.delete_funder, name='delete_funder'),
    url(r'^(?P<article_id>\d+)/files/$', views.submit_files, name='submit_files'),
    url(r'^(?P<article_id>\d+)/funding/$', views.submit_funding, name='submit_funding'),
    url(r'^(?P<article_id>\d+)/funding/done/$', views.submit_funding_done, name='submit_funding_done'),

    url(r'^submissions/$', views.submit_submissions, name='submission_submissions'),
    url(r'^(?P<article_id>\d+)/review/$', views.submit_review, name='submit_review'),

    url(r'^manager/article/settings/article/(?P<article_id>\d+)/publishernotes/order/$', views.publisher_notes_order,
        name='submission_article_publisher_notes_order'),

    url(r'^manager/configurator/$', views.configurator, name='submission_configurator'),

    url(r'^manager/additional_fields/$', views.fields, name='submission_fields'),
    url(r'^manager/additional_fields/(?P<field_id>\d+)/$', views.fields, name='submission_fields_id'),

    url(r'^manager/licences/$', views.licenses, name='submission_licenses'),
    url(r'^manager/licences/(?P<license_pk>\d+)/delete/',
        views.delete_license,
        name='submission_delete_license'),
    url(r'^manager/licences/(?P<license_pk>\d+)/', views.licenses, name='submission_licenses_id'),



]
