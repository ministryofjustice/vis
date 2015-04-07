from django.conf import settings

def globals(request):
    context = {
        'GA_ID': settings.GA_ID
        }
    return context
