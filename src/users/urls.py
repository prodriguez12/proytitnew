from django.conf.urls import url, include
from .views import SignUpView

urlpatterns = [
    url(r'signup/', SignUpView.as_view(), name='signup'),
]