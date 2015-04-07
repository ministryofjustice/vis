from django.conf import settings

def globals(request):
    context = {
        'GA_ID': settings.GA_ID,
        'PINGDOM_ID': settings.PINGDOM_ID
        }
    return context
