
from django.urls import path
from dashboard import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('seller',views.seller,name='seller'),
    path('buyer',views.buyer,name='buyer'),
    path('gallery',views.gallery,name='gallery'),
    
]
