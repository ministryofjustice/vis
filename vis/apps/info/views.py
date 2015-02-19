from django.views.generic import ListView
from info.models import GlossaryItem


class GlossaryItemList(ListView):
    queryset = GlossaryItem.objects.order_by('name')
