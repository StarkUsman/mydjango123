from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import RecipeIngredient, Recipe
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password = 'abc123')
    
    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)
        
class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password = 'abc123')
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chick',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Grilled Chick Tacos',
            user = self.user_a
        )
    
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        # print(qs)
        self.assertEqual(qs.count(), 2)
        
    def test_user_forward_reverse_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        # print(qs)
        self.assertEqual(qs.count(), 2)
        