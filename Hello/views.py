"""
    to render html pages
"""

import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article



def home_view(request, *args, **kwargs):
    
    """
    take in a request(django sends)
    return HTML as response(we pick the return)
    """
    # print(100*1000)
    print(args, kwargs)
    name = "Faraz"
    rand_id = random.randint(1,3) #pseudo random
    
    article_obj = Article.objects.get(id = rand_id)
    
    
    # from the database
    article_queryset = Article.objects.all()

        
    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,
        "name": name
    }
    
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>Hello {title} (id:{id})</h1>
    # <p>Hello {content}</p>
    # """.format(**context) #unpacking key-value context pair
    return HttpResponse(HTML_STRING)