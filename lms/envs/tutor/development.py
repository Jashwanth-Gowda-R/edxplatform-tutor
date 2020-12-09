# -*- coding: utf-8 -*-
import os
from lms.envs.devstack import *

####### Settings common to LMS and CMS
import json
import os

# Mongodb connection parameters: simply modify `mongodb_parameters` to affect all connections to MongoDb.
mongodb_parameters = {
    "host": "mongodb",
    "port": 27017,
    
    "user": None,
    "password": None,
    
    "db": "openedx",
}
DOC_STORE_CONFIG = mongodb_parameters
CONTENTSTORE = {
    "ENGINE": "xmodule.contentstore.mongo.MongoContentStore",
    "ADDITIONAL_OPTIONS": {},
    "DOC_STORE_CONFIG": DOC_STORE_CONFIG
}
# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)
DATA_DIR = "/openedx/data/"
for store in MODULESTORE["default"]["OPTIONS"]["stores"]:
   store["OPTIONS"]["fs_root"] = DATA_DIR


DEFAULT_FROM_EMAIL = ENV_TOKENS.get("DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
DEFAULT_FEEDBACK_EMAIL = ENV_TOKENS.get("DEFAULT_FEEDBACK_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
SERVER_EMAIL = ENV_TOKENS.get("SERVER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
TECH_SUPPORT_EMAIL = ENV_TOKENS.get("TECH_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
CONTACT_EMAIL = ENV_TOKENS.get("CONTACT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BUGS_EMAIL = ENV_TOKENS.get("BUGS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
UNIVERSITY_EMAIL = ENV_TOKENS.get("UNIVERSITY_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PRESS_EMAIL = ENV_TOKENS.get("PRESS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PAYMENT_SUPPORT_EMAIL = ENV_TOKENS.get("PAYMENT_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BULK_EMAIL_DEFAULT_FROM_EMAIL = ENV_TOKENS.get("BULK_EMAIL_DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_MANAGER_EMAIL = ENV_TOKENS.get("API_ACCESS_MANAGER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_FROM_EMAIL = ENV_TOKENS.get("API_ACCESS_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])

# Get rid completely of coursewarehistoryextended, as we do not use the CSMH database
INSTALLED_APPS.remove("coursewarehistoryextended")
DATABASE_ROUTERS.remove(
    "openedx.core.lib.django_courseware_routers.StudentModuleHistoryExtendedRouter"
)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/media/"

# Add your MFE and third-party app domains here
CORS_ORIGIN_WHITELIST = []

# Video settings
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT

GRADES_DOWNLOAD = {
    "STORAGE_TYPE": "",
    "STORAGE_KWARGS": {
        "base_url": "/media/grades/",
        "location": "/openedx/media/grades",
    },
}

ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = "/openedx/data/ora2"
ORA2_FILEUPLOAD_CACHE_NAME = "ora2-storage"

# Change syslog-based loggers which don't work inside docker containers
LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "all.log"),
    "formatter": "standard",
}
LOGGING["handlers"]["tracking"] = {
    "level": "DEBUG",
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "tracking.log"),
    "formatter": "standard",
}
LOGGING["loggers"]["tracking"]["handlers"] = ["console", "local", "tracking"]
# Disable django/drf deprecation warnings
import logging
import warnings
from django.utils.deprecation import RemovedInDjango30Warning, RemovedInDjango31Warning
from rest_framework import RemovedInDRF310Warning, RemovedInDRF311Warning
warnings.simplefilter('ignore', RemovedInDjango30Warning)
warnings.simplefilter('ignore', RemovedInDjango31Warning)
warnings.simplefilter('ignore', RemovedInDRF310Warning)
warnings.simplefilter('ignore', RemovedInDRF311Warning)

# Email
EMAIL_USE_SSL = False
# Forward all emails from edX's Automated Communication Engine (ACE) to django.
ACE_ENABLED_CHANNELS = ["django_email"]
ACE_CHANNEL_DEFAULT_EMAIL = "django_email"
ACE_CHANNEL_TRANSACTIONAL_EMAIL = "django_email"
EMAIL_FILE_PATH = "/tmp/openedx/emails"

LOCALE_PATHS.append("/openedx/locale/contrib/locale")
LOCALE_PATHS.append("/openedx/locale/user/locale")

# Allow the platform to include itself in an iframe
X_FRAME_OPTIONS = "SAMEORIGIN"


JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "4mbqBH9VglsytD67zLaTxYLP"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = json.dumps(
    {
        "kid": "openedx",
        "kty": "RSA",
        "e": "AQAB",
        "d": "BbCbAkvywwB_Jok1LUPZFbEwJJUMyGwRFWgaFQ6smDmzQ6msum5JHO8MuDKEHkrfRfVeL80xdPOj_U-XVWO5sYPmTTWOyFCyAK0mi8cP72TNyQbZMDE-FEjzAdg8ggAO2ROF2LQ6ATo3TzkZQuJcApca4rU06Lcuog7ML3V3kwuP3K9XQXgUlDro23Ms-cC-oM0KMZPwVDctOw66U5krs9BFl4pa685X8yJ_sa4OyQqmIyHPDOJ9uefrlI37jCSSxq5_vCKRkvITXgYJFL9s2FZPOW51EuuPN02mW3QO4uFLQR7XtlFo8I_N1qynzLGgRuS5lCIFsbQL5Q81uwswbQ",
        "n": "xuDUS8Upf9SabHTVVGGIVYHSF-tu7fUChbEDklSaZ847cQqRA0dYOwEudH6---cXdepykxkoTA_3ZEt0UuI_P260GjH4Vje_vlkvxuAmBL43IucLM4gpKyX_BCEW1VeiOE1nYv8kG1Y50EThAS1QjDxGst8LDG_eTxyRlF1BvhR3rAKaX0Wknyg8PXN5TPEZnZEcKQyW79OVkwlKwd34lBDsX501As8WgrpNT9PUoSpjn5Bn0B6K0bgjN1_-lyz6drd_tpo1I0bKcQI7Go3lVgcIt6RLiYPYSWZ3iUF0LwB788lr5grjkAZsToH6q_IXCrWBicyPwwpD0TeFtOkoMQ",
        "p": "yIryWBBUIOaho6wiQg5KxNXunqnzTLdrPvzF2dThXdBiprbGM30NYQgXt6XjpiSQK1Z2vCD_yh1dAqzys20K16GTFUl5Kq1WmsjUH5uBF7rVNa_2S1P3qQXqK8BHS5wRkQiw0EPojF2F4P-_Q3CKoZ4x6dxXU4A8Us3HBD_W1T8",
        "q": "_eALwvLfwjXu5UATTt_vDSlwHDNOASdojOUvdG5aObD6rOeEETOp_EZIFh4GgnDwEy2qGRbPwMluLOaClDFaZhvUNrrpX_8zujmIemqjLpPM_G9aGbB6R7jJNez3G7-OGN-dNGRnhx_VAO8erKvZd8-AHVz1MNRiaHc0mKIjdo8",
    }
)
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "xuDUS8Upf9SabHTVVGGIVYHSF-tu7fUChbEDklSaZ847cQqRA0dYOwEudH6---cXdepykxkoTA_3ZEt0UuI_P260GjH4Vje_vlkvxuAmBL43IucLM4gpKyX_BCEW1VeiOE1nYv8kG1Y50EThAS1QjDxGst8LDG_eTxyRlF1BvhR3rAKaX0Wknyg8PXN5TPEZnZEcKQyW79OVkwlKwd34lBDsX501As8WgrpNT9PUoSpjn5Bn0B6K0bgjN1_-lyz6drd_tpo1I0bKcQI7Go3lVgcIt6RLiYPYSWZ3iUF0LwB788lr5grjkAZsToH6q_IXCrWBicyPwwpD0TeFtOkoMQ",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://local.overhang.io/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "4mbqBH9VglsytD67zLaTxYLP"
    }
]


######## End of settings common to LMS and CMS

######## Common LMS settings
LOGIN_REDIRECT_WHITELIST = ["studio.local.overhang.io"]

# This url must not be None and should not be used anywhere
LEARNING_MICROFRONTEND_URL = "http://learn.openedx.org"

# Fix media files paths
PROFILE_IMAGE_BACKEND["options"]["location"] = os.path.join(
    MEDIA_ROOT, "profile-images/"
)

COURSE_CATALOG_VISIBILITY_PERMISSION = "see_in_catalog"
COURSE_ABOUT_VISIBILITY_PERMISSION = "see_about_page"

# Allow insecure oauth2 for local interaction with local containers
OAUTH_ENFORCE_SECURE = False

# Create folders if necessary
for folder in [DATA_DIR, LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE, ORA2_FILEUPLOAD_ROOT]:
    if not os.path.exists(folder):
        os.makedirs(folder)



######## End of common LMS settings

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

SESSION_COOKIE_DOMAIN = ".local.overhang.io"

LMS_BASE = "local.overhang.io:8000"
LMS_ROOT_URL = "http://{}".format(LMS_BASE)
LMS_INTERNAL_ROOT_URL = LMS_ROOT_URL
SITE_NAME = LMS_BASE
CMS_BASE = "studio.local.overhang.io:8001"
CMS_ROOT_URL = "http://{}".format(CMS_BASE)
LOGIN_REDIRECT_WHITELIST.append(CMS_BASE)

FEATURES['ENABLE_COURSEWARE_MICROFRONTEND'] = False
COMMENTS_SERVICE_URL = "http://forum:4567"

LOGGING["loggers"]["oauth2_provider"] = {
    "handlers": ["console"],
    "level": "DEBUG"
}


