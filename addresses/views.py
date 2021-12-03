from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'addresses/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiaG91c3NhbWNoMDEiLCJhIjoiY2t2czVjYnlmMHk0OTJycXB6MzF0Y21xYyJ9.aHq_Gn0uxs5Hczf9EPwpVA'
        context['addresses'] = Address.objects.all()
        return context

class AddressView1(CreateView):

    model = Address
    fields = ['address']
    template_name = 'addresses/home2.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiaG91c3NhbWNoMDEiLCJhIjoiY2t2czVjYnlmMHk0OTJycXB6MzF0Y21xYyJ9.aHq_Gn0uxs5Hczf9EPwpVA'
        context['addresses'] = Address.objects.all()
        return context
