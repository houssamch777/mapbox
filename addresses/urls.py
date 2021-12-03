from django.urls import path
from .views import AddressView, AddressView1#AddressView1


urlpatterns = [
    path('', AddressView.as_view(), name='home'),
    path('home/', AddressView1.as_view(), name='home1'),
    
]