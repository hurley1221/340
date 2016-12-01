from django.http import HttpResponse
from .models import Modules

def index(request):
    all_modules = Modules.objects.all()
    html = ''
    for modules in all_modules:
        url = '/music/' + str(modules.id) + '/'
        html += '<a href="' + url + '">' + modules.ModuleCode + '</a><br>'
    return HttpResponse(html)