from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProjectTestCase(TestCase):
    
    def setUp(self):
        """
        Create a project for testing
        """
        self.user=User(username='kibe',email='adnang680@gmail.com',password='qwerty1234')
        self.project=Project(image='SayCheese.jpg',title='SayCheese',description='SayCheese',url='github.com', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.project,Project))

    def test_save(self):
        self.user.save()
        self.project.save_project()

        users = User.objects.all()
        projects = Project.objects.all()

        self.assertTrue(len(projects) > 0)
        self.assertTrue(len(users) > 0)