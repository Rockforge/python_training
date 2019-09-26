from django.test import TestCase
from .forms import CommentForm
from .models import Comment



class CommentTestCase(TestCase):
    # def setUp(self):
        # Comment.objects.create(name='spam', comments='shit', email='spam@spam.com')

    def test_CommentsAreCensored(self):
        POST = {'name':'spam', 'comments':'shit', 'email':'spam@spam.com'}
        form = CommentForm(POST)
        if not form.is_valid():
            self.fail('Data is not valid')
        
        form.clean()
        self.assertIn('shit', form.cleaned_data['comments'])


