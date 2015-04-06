from django.test import TestCase
from login.models import User
from django.test.client import Client
from django.test.client import RequestFactory


from login.views import ListUserView
# Create your tests here.


class UserTests(TestCase):


   def test_str(self):
   
      user = User(username='hans', email = 'hansjhe2@gmail.com', password1 = 'hanshe', password2 = 'hanshe')
      
      self.assertEquals(str(user), 'hans hansjhe2@gmail.com',) 
      
class UserListViewTests(TestCase):
    """Contact list view tests."""

    def test_users_in_the_context(self):

        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])

        User.objects.create(username='foo', email='hjh@gg.com', password1='aa', password2='aa')
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_users_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ListUserView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        User.objects.create(username='foo', email='hjh@gg.com', password1='aa', password2='aa')
        response = ListUserView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)