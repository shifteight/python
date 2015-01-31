# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse


def hello_world(request):
    todos = [
        {
            'title': 'Mow the lawn',
            'importance': 'Minor'
        },
        {
            'title': 'Backup your PC',
            'importance': 'High'
        },
        {
            'title': 'Buy some Milk',
            'importance': 'Medium'
        },
        {
            'title': 'See the film',
            'importance': 'High'
        }
    ]
    t = loader.get_template('index.tmpl')
    c = Context({
        'todos': todos,
    })

    return HttpResponse(t.render(c))
