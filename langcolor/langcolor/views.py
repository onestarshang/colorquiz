
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return render_to_response('404.html',{}, 
        context_instance=RequestContext(request))
