#!/bin/sh

. /etc/janeway/djangorc
bin/debug.sh manage runserver localhost:8133
