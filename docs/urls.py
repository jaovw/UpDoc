from django.urls import path


from .views import teste, index

urlpatterns = [
    
    path('',index, name='index'),
    path('teste/', teste, name='list'),
    
]


