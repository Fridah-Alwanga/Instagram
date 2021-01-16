from django.test import TestCase
from.models import Profile

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.You = Profile(name = 'You', profile_pic = 'image.jpg', bio='Using Instagram')
        self.You.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.You, Profile))

    def test_save_method(self):
        self.You.save_profile()
        name = Profile.objects.all()

    def test_delete_method(self):
        self.profile_pic.delete_profile_pic()
        Profile = Profile.objects.all()
        self.assertTrue(len(Locations)==2) 



class PostTestCase(TestCase):

    def setUp(self):
        self.swimming = Profile(image= 'image.jpg', title = 'swimming', user='User')
        self.swimming.save()


    def tearDown(self):
        Post.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.swimming, Post))


    def  test_save_method(self):
        self.You.save_post()
        tittle = Post.objects.all()