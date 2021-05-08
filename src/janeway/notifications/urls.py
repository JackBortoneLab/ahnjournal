from django.conf.urls import url

from notifications import views

urlpatterns = [
    url(r'^i/notifications/$', views.home, name='notifications_home'),
    url(r'^i/notifications/(?P<notification_id>\d+)/$', views.notification_details, name='notification_details'),
]
