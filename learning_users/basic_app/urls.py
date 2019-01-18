from django.conf.urls import url
from basic_app import views

##TEMPLATE URLs
app_name = 'basic_app'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
