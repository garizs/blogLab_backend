from django.shortcuts import redirect
from django.views.generic import RedirectView


def view_404(request, *args, **kwargs):
    url = request.path
    if url.find('static') == -1 and url.find('media') == -1:
        return redirect(to='admin/')

