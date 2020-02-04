"""
View for current operations
"""
from django.shortcuts import render
from django.views import View


class CurrentView(View):
    """
    View for current operations
    """

    def get(self, request):
        return render(request, 'base.html')
