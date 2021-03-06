# -*- coding: utf-8 -*-
"Zendesk"
from django.http import JsonResponse
from django.http.response import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.vary import vary_on_headers
from django.views.generic.base import View
from wagtail.wagtailcore.models import Page
from zendesk.client import ZendeskClient


def get_url_from_request(request):
    return request.META.get('HTTP_REFERER')

def get_user_agent_from_request(request):
    return request.META.get('HTTP_USER_AGENT')

class ZendeskView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ZendeskView, self).dispatch(*args, **kwargs)

    @vary_on_headers('HTTP_X_REQUESTED_WITH')
    def post(self, request):
        "Create a new Zendesk ticket"
        zendesk_client = ZendeskClient()
        response = zendesk_client.create_ticket(
            feedback_type=request.POST.get('feedback_type', 'Comment'),
            feedback_data={
                'comments': request.POST.get('comments'),
                'user': request.user if hasattr(request, 'user') and request.user.is_authenticated() else 'Anonymous',
                'url': request.POST.get('url', get_url_from_request(request)),
                'user_agent': request.POST.get('user_agent', get_user_agent_from_request(request))
            })
        if request.is_ajax():
            return JsonResponse(response['json'], status=response['status'])
        else:
            confirm_page = Page.objects.filter(slug='feedback-confirm').first()
            if not confirm_page:
                raise Http404()
            return redirect(confirm_page.url)
