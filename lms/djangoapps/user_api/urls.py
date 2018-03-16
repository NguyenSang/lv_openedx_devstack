from django.conf.urls import include, patterns, url

from . import views

USER_URLS = patterns(
    '',
    url(r'^$', views.UserApiView.as_view(), name='create_user_api'),

)

urlpatterns = patterns(
    '',
    url(r'^user_api/', include(USER_URLS, namespace='user_api')),
)
