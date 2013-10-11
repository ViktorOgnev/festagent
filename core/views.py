from django.utils import simplejson
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Fest


def fest_list(request):
    # in production would have a cache hit first
    context = {}
    template = 'core/fest_list.html'
    
    ordering = request.REQUEST.get('ordering', '')
    if ordering in ['biginning_date', 'name']:
        festivals = Fest.objects.values().order_by(ordering)
        if request.is_ajax():
            html = render_to_string('core/fest_list_div.html',
                                    {'festivals': festivals})
            json_response = simplejson.dumps(
                {'success': 'True', 'html': html})
            return HttpResponse(json_response,
                                content_type="application/javascript")

    else:
        context['festivals'] = Fest.objects.values()

    return render_to_response(template, context,
                              context_instance=RequestContext(request))
