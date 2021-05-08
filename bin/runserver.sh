#!/bin/sh
set -x
. /etc/janeway/djangorc
/usr/local/bin/uwsgi --uwsgi-socket localhost:8000 --wsgi-file "$ROOTDIR/www-bin/dispatch-django.wsgi"
