#!/bin/sh
#########
# debug.sh main debug script for the gthc.org web app
# Copyright (C) 2012 Etienne Robillard <erob@gthcfoundation.org>
# All rights reserved.

# Enable this option if you're debugging the script
# itself.
#set -x

ulimit -n 1024

# Set the path as necessary.
export PATH="/bin:/usr/bin:/usr/local/bin"

# Include system config if it exists
[ -r ./djangorc ] && . ./djangorc

FIND=/usr/bin/find
HTTPSERVER=/usr/local/bin/httpserver.py

# Required for backward-compatibility
DJANGO_SETTINGS_MODULE='local_settings'
export DJANGO_SETTINGS_MODULE ROOTDIR 

clean() {
    # ensure that we start clean
    echo "Now cleaning up $ROOTDIR of old files"
    $FIND $ROOTDIR -name __pycache__ -type d -delete || true
    $FIND $ROOTDIR -name "*.py[co]" -exec rm -f '{}' ";" || true
    $FIND $ROOTDIR -name "*.sw[po]" -exec rm -f '{}' ";" || true
    $FIND $DJANGO_HOME -name "*.py[co]" -exec rm -f '{}' ";" || true
    [ -e /var/db/feeds/feed_cache ] && rm -rf /var/db/feeds/feed_cache || true
    [ -x /var/run/nginx ] && rm -rf /var/run/nginx/* || true
    #clean_memcache;
}
clean_memcache(){
    # clean up memcache..
    echo "Cleaning up memcached..."
    [ -x "$BINDIR/cleanMemcache.py" ] && $PYTHON $BINDIR/cleanMemcache.py
}

manage() {
    shift;
    $PYTHON $BINDIR/manage.py $@
}
#create_user() {
#    shift;
#    python $BINDIR/create_user.py $@
#}
dump() {
    shift;
    eval $BINDIR/database_dump.sh $@;
}
daemonize() {
    shift;
    $PYTHON $BINDIR/daemonize.py $@;
}
initdb() {
    echo -n "Initializing memcached pool..."
    #generate the photo_gallery store
    $PYTHON $ROOTDIR/lib/tm/utils/photo_gallery.py
    #generate the sitemap
    echo "done!"
}
runserver() {
    # clean && initdb || true;
    local err=3
    shift;
    #clean;
    while test "$err" -eq 3 ; do
        #TODO: Switch to httpserver.py and fix logging...
        #$PYTHON $BINDIR/runserver.py $@
        $PYTHON $PYTHONFLAGS $HTTPSERVER --disable-auth --settings=$DJANGO_SETTINGS_MODULE --wsgi-app=janeway.wsgi.application $@
        err="$?"
    done
}
respawn(){
    shift;
    clean;
    #eval "$BINDIR/respawn.sh" "$@"
    eval $PYTHON "$ROOTDIR/www-bin/dispatch-debug.fcgi"
}
respawn_hgwebdir(){
    shift;
    eval "$BINDIR/respawn-hgwebdir.sh" "$@"
}
moinmoin_start(){
    shift;
    #eval "$BINDIR/moinmoin.sh" "$@"
    eval $PYTHON "$ROOTDIR/www-bin/moinmoin.fcgi"
    #python2.7 $BINDIR/moinmoin_server.py
} 
comment_manager_start(){
    shift;
    eval "$PYTHON $BINDIR/CommentManager.py $@";
}
upgradedb(){
    shift;
    eval "$BINDIR/upgradedb.sh" "$@";
}
repairdb(){
    shift;
    eval schevo db repair "$@";
}    
syncdb(){
    shift;
    eval "$BINDIR/syncdb.sh" "$@";
}
schevo(){
    shift;
    eval /usr/local/bin/schevo $@ || true;
}
gtk(){
    shift;
    eval $HOME/bin/schevo-editor $@ || true;
}    
shell(){
    # start a shell (ipython) for l34t hak3ng!
    #shift;
    #if test -x `which ipython` ; then
    # ipython "$@"
    #fi;     
    eval "$PYTHONHOME/bin/schevo" "$@" || true;
}
create_sitemap(){
    # recreate the sitemap.xml file
    shift;
    eval "$PYTHON $BINDIR/create_sitemap.py" "$@";
}
runtest(){
    # run a test suite
    shift;
    eval "$PYTHON $ROOTDIR/tests/$1";
}
case $1 in manage)
    manage "$@"
    ;; 
clean)
    clean
    ;;
create_sitemap)
    create_sitemap "$@"
    ;;
daemonize)
    daemonize "$@"
    ;;
dump)
    dump "$@"
    ;;
respawn)
    #clean;
    respawn "$@"
    ;;
respawn-hgwebdir)
    respawn_hgwebdir $@
    ;;
repairdb)
    repairdb "$@"
    ;;
runserver)
    #clean; # start clean
    runserver "$@"
    ;;
runtest)
    runtest "$@"    
    ;;
moinmoin)
    clean;
    moinmoin_start "$@"
    ;;
manage_comments)
    clean;
    comment_manager_start "$@"
    ;;
upgradedb)
    upgradedb "$@"
    ;;
syncdb)
    syncdb "$@"
    ;;
shell)
    shell "$@"
    ;;
schevo)
    schevo "$@"
    ;;
schevo-editor)
    gtk "$@"
    ;;
initmemcache)
    initmemcache "$@"
    ;;
*)
    #echo "Usage: debug.sh <clean|manage|respawn|runserver|moinmoin> [options]"
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Available subcommands: "
    
    echo "clean, dump, manage, runserver, moinmoin, manage_comments, upgradedb"
    echo "Server commands: respawn, respawn-hgwebdir"
    exit 0;
esac        
