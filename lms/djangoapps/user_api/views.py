import logging
from django.http import HttpResponse
import requests
from edx_rest_api_client import exceptions
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE, HTTP_409_CONFLICT
from rest_framework.views import APIView

from enrollment.views import EnrollmentCrossDomainSessionAuth
from openedx.core.djangoapps.commerce.utils import ecommerce_api_client
from openedx.core.djangoapps.embargo import api as embargo_api
from openedx.core.djangoapps.user_api.preferences.api import update_email_opt_in
from openedx.core.lib.api.authentication import OAuth2AuthenticationAllowInactiveUser
from openedx.core.lib.log_utils import audit_log

log = logging.getLogger(__name__)
SAILTHRU_CAMPAIGN_COOKIE = 'sailthru_bid'


class UserApiView(APIView):
    authentication_classes = (EnrollmentCrossDomainSessionAuth, OAuth2AuthenticationAllowInactiveUser)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>sang<h1>")
