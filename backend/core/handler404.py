"""
    Модуль редиректа если 404
"""
from django.shortcuts import redirect


def view_404(request, exception):
    """
        Метод редиректа
    """
    return redirect(to='/admin/')
