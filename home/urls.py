from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('review/',views.review,name='review'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]