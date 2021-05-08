#!/usr/bin/env python

import unittest
import datetime

import django

django.setup()

class ModelTestCase(unittest.TestCase):

    def setUp(self):
        pass

class PreprintManagerTestCase(ModelTestCase):

    def test_preprint_index(self):
        # get a list of published preprints
        pass

    def test_preprint_last_updated(self):
        # retrieve the most recent updated preprints since April 1st 2021
        from submission.models import Article
        objs = Article.objects.filter(stage='preprint_published')
        print(objs)

if __name__ == '__main__':
    unittest.main()

