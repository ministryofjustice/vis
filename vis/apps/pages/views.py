from django.views.generic import TemplateView


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
