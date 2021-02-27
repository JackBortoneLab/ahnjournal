AHNJournal
==========

Requirements :

* Python 3
* uWSGI 2.0
* nginx 
* Django 1.11.29

To start the dev server :

 $ sudo mkdir /etc/janeway
 $ sudo mv djangorc /etc/janeway/
 $ source /etc/janeway/djangorc
 $ debug.sh manage runserver localhost:8133 

To start the uWSGI backend :

 $ sh -x ./runserver.sh & 

Contact :

Jack Bortone <info@open-neurosecurity.org> 
