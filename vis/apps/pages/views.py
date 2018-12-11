import itertools

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import SearchForm


def pcc_search(request):
    template = 'pages/pcc_search.jade'
    q = request.GET.get('q')
    errors = []
    if q:
        template = 'pages/pcc_no_results.jade'
        form = SearchForm(data=request.GET)
        if form.is_valid():
            postcode = form.cleaned_data['q']
            pcc = form.cleaned_data['pcc']
            return redirect(u'%s%s/' % (pcc.url, postcode))
        else:
            errors = list(itertools.chain.from_iterable(form.errors.values()))

    return render(request, template, {
            'q': q,
            'title': 'Find local support',
            'errors': errors
        }
    )


class ErrorHandler(TemplateView):
    template_name = None
    status = None

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()

        def view(request):
            r = v(request)
            r.render()
            return r

        return view

    # must also override this method to ensure the 500 status code is set
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=self.status)


class Handler500(ErrorHandler):
    template_name = '500.jade'
    status = 500


class Handler404(ErrorHandler):
    template_name = '404.jade'
    status = 404
