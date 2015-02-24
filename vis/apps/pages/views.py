import itertools

from django.shortcuts import render, redirect

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
