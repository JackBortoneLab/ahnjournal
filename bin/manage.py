#!/usr/bin/env python

import os
import sys

import django
django.setup()

#sys.path.append(os.path.join(os.environ['ROOTDIR'], 'src/janeway'))
#from django.conf import settings

from janeway.utils import load_janeway_settings
os.environ.setdefault("JANEWAY_SETTINGS_MODULE", "local_settings")

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    load_janeway_settings()

    execute_from_command_line(sys.argv)
