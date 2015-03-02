import itertools

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import SearchForm


def pcc_search(request):
    q = request.POST.get('q')
    errors = None
    if request.method == 'POST':
        form = SearchForm(data=request.POST)
        if form.is_valid():
            pcc = form.cleaned_data['pcc']
            return redirect(pcc.url)
        else:
            errors = list(itertools.chain.from_iterable(form.errors.values()))
    else:
        return redirect('/')

    return render(request, 'pages/result_list.jade', {
            'q': q,
            'errors': errors
        }
    )


class Handler500(TemplateView):
    template_name = '500.html'

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
        return self.render_to_response(context, status=500)
