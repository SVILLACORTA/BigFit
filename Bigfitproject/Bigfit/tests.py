from django.test import TestCase
from .models import *
from datetime import *
import pytest


@pytest.mark.django_db
class testModel(TestCase):

    @staticmethod
    def create_user():
        user = User.objects.create()
        user.username = 'TestUser'
        user.password = 'testuser'
        user.first_name = 'Test'
        user.last_name = 'User'
        user.target_weight = 120
        user.feet = 5
        user.inches = 4
        user.date_of_birth = datetime.strptime('01/07/1985', '%m/%d/%Y')
        user.zip_code = '91709'
        user.gender = 'F'
        user.save()

        return user

    def test_user(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, User))
        assert user.username == 'TestUser'

    def test_weightracker(self):
        user = self.create_user()
        wt = WeightTracker.objects.create(weight=123, user=user)
        wt.save()

        self.assertTrue(isinstance(wt, WeightTracker))
        assert wt.weight == 123


