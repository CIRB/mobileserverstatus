from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from mobileserverstatus.models import Message

def get_status(request):
    if request.method == 'POST':
        return PermissionDenied

    message = Message.objects.all()[0]

    response = '{ "status" : "%s", "version" : %d }' %(message.status, message.version)
    return HttpResponse(response)
