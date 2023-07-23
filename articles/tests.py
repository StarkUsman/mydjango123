from django.test import TestCase
from django.utils.text import slugify
from .utils import slugify_instance_title


# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    
    def setUp(self):
        self.no_of_articles = 500
        for i in range(0,self.no_of_articles):
            Article.objects.create(title='Hello World', content = 'something123')
            
        
    def test_quaryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
        
    def test_quaryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.no_of_articles)
        
    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        sluggified_title = slugify(title)
        self.assertEqual(slug, sluggified_title)

    def test_hello_world_unique_slug(self):
        qs = Article.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            sluggified_title = slugify(title)
            self.assertNotEqual(slug, sluggified_title)
            
    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slug = []
        for i in range(0,25):
            instance = slugify_instance_title(obj, save = False)
            new_slug.append(instance.slug)
        
        unique_slugs = list(set(new_slug))
        self.assertEqual(len(new_slug), len(unique_slugs))
        
    def test_slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))
        
    def test_article_search_manager(self):
        qs = Article.objects.search(query='hello world')
        self.assertEqual(qs.count(), self.no_of_articles)
        qs = Article.objects.search(query='hello')
        self.assertEqual(qs.count(), self.no_of_articles)
        qs = Article.objects.search(query='something123')
        self.assertEqual(qs.count(), self.no_of_articles)