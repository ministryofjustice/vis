import os

from django.http import JsonResponse


def ping(request):
    return JsonResponse({
        "commit_id": os.environ.get('GIT_SHA', ''),
        "build_date": os.environ.get('DEPLOY_DATETIME', '')
    })
