from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login , name='login'),
    url(r'^signupHandler/$', views.signupHandler , name='signupHandler'),
    url(r'^loginHandler/$', views.loginHandler , name='loginHandler'),
    url(r'^toolput/$', views.toolput , name='toolput'),
    url(r'^toolget/$', views.toolget , name='toolget'),
    url(r'^loginpage/$',views.loginpage, name='loginpage'),
]
