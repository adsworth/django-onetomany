"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.contrib.auth.models import User
from django.db import models
from django.db.utils import IntegrityError
from django.test import TestCase

from onetomany.models import OneToManyField

class Team(models.Model):
    name = models.CharField(max_length=20)
    members = OneToManyField(User)


class OneToManyTest(TestCase):
    def setUp(self):
        self.u1 = User(username='user1')
        self.u1.save()
        self.u2 = User(username='user2')
        self.u2.save()
        self.u3 = User(username='user3')
        self.u3.save()
        
        self.t1 = Team(name='Team 1')
        self.t1.save()
        self.t2 = Team(name='Team 2')
        self.t2.save()
    def test_add_from_own_side(self):
        
        self.t1.members.add(self.u1)
        self.t1.members.add(self.u2)

        self.t2.members.add(self.u3)
        
        self.assertRaisesMessage(IntegrityError, 
                                "column user_id is not unique",
                                self.t2.members.add,
                                self.u1)

    def test_add_from_other_side(self):
        """
        That a oneTomany field only allows a to instance to be related to one from instance.
        """
        
        self.u1.team_set.add(self.t1)
        self.u2.team_set.add(self.t1)

        self.u3.team_set.add(self.t2)

        self.assertRaisesMessage(IntegrityError, 
                                "column user_id is not unique",
                                self.u1.team_set.add,
                                self.t2)

