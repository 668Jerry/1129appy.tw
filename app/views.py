from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('index.html', context_dict, context)