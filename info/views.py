from django.http import HttpResponse
from django.template import loader
from .models import Modules, Marks


def index(request):                                         ##declare function
    all_marks = Marks.objects.all()                         ##set all_marks to the object
    template = loader.get_template('info/info.html')        ##loader html template from info.html
    context = {'all_marks': all_marks,}                     ##sets the all_marks data = context to use in http function
    return HttpResponse(template.render(context, request))  ##return http with the variables above

