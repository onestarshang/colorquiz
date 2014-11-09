# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from colorquiz.models import LanguageColor 


def index(request):
    quiz_list, answer_str = LanguageColor.generate_quiz()
    return render_to_response('index.html', 
        {'quiz_list':quiz_list,
         'answer_str':answer_str}, 
        context_instance=RequestContext(request))

def submit_answer(request):
    #print '****************'
    #print request.POST
    score =1 
    post_answer = request.POST
    colornum_list = LanguageColor.all_colornum_list()
    #validate
    for k, v in post_answer.items():
        if k in colornum_list:
            a_color = LanguageColor.get_color_by_language_id(v[0])
            if a_color == k:
                score += 1
    return render_to_response('result.html', 
        {'score':score},
        context_instance=RequestContext(request))
    
