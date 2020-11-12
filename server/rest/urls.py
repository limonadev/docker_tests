from django.conf.urls import url 
from rest import views 
 
urlpatterns = [ 
    url('code', views.send_code),
]