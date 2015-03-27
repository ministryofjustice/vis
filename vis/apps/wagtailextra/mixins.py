class JadePageMixin(object):
    def get_template(self, request, *args, **kwargs):
        template_path = super(JadePageMixin, self).get_template(request, *args, **kwargs)
        return template_path.replace('.html', '.jade')


class ObjectListMixin(object):
    object_class = None
    subpage_types = []

    def get_object_list_queryset(self):
        return self.object_class.objects.all()

    def get_context(self, request, *args, **kwargs):
        context = super(ObjectListMixin, self).get_context(
            request, *args, **kwargs
        )

        context['object_list'] = self.get_object_list_queryset()
        return context
