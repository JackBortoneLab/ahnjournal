#!/bin/sh

. /etc/janeway/djangorc.devel
bin/debug.sh manage runserver localhost:8133
