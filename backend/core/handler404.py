"""
    Модуль редиректа если 404
"""
from django.http import HttpResponseNotFound
from django.shortcuts import redirect


def view_404(request, exception):
    """
        Метод редиректа
    """
    url = request.path
    if url.find('static') == -1 and url.find('media') == -1:
        return redirect(to='/admin/')
    return HttpResponseNotFound(exception)
