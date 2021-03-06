__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"

import json
from urllib.parse import urlencode

from django.conf import settings
from django.urls import reverse
import requests
from requests.exceptions import HTTPError

from utils import logic
from utils.logger import get_logger

logger = get_logger(__name__)


def retrieve_tokens(authorization_code, site=None):
    """ Retrieves the access token for the given code

    :param authorization_code: (str) code provided by ORCID
    :site: Object implementing the AbstractSiteModel interface
    :return: ORCID ID or None
    """

    request = logic.get_current_request()
    redirect_uri = build_redirect_uri(request)
    access_token_req = {
        "code": authorization_code,
        "client_id": settings.ORCID_CLIENT_ID,
        "client_secret": settings.ORCID_CLIENT_SECRET,
        #"redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }

    #content_length = len(urlencode(access_token_req))
    #access_token_req['content-length'] = str(content_length)
    access_token_req['Accept'] = 'application/json'
    base_url = settings.ORCID_TOKEN_URL

    logger.info("Connecting with ORCID on %s" % base_url)
    r = requests.post(base_url, data=access_token_req)
    try:
        r.raise_for_status()
    except HTTPError as e:
        logger.error("ORCID request failed: %s" % str(e))
        orcid_id = None
    else:
        logger.info("OK response from ORCID")
        if r.ok:
            logger.info(r.text)
            orcid_id = json.loads(r.text).get("orcid")


    return orcid_id


def build_redirect_uri(request):
    """ builds the landing page for ORCID requests
    :site: Object implementing the AbstractSiteModel interface
    :return: (str) Redirect URI for ORCID requests
    """

    path = reverse("core_login_orcid")

    try:
        return request.site_type.site_url(path)
    except:
        return settings.DEFAULT_HOST
