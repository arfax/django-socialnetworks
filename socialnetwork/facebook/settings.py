from django.core.exceptions import ImproperlyConfigured

from socialnetwork.base.settings import CONFIGURATION


# Tries to get the Facebook configuration, if the configuration is not
# provided or is incorrect raises an ImproperlyConfigured exception.
FACEBOOK = CONFIGURATION.get('FACEBOOK', None)

if not FACEBOOK:
    raise ImproperlyConfigured('You have socialnetwork.facebook in your '
        'ISTALLED_APPS, but you do not specify any "FACEBOOK" settings '
        'inside SOCIALNETWORK_CONFIGURATION.')

else:
    APP_ID = FACEBOOK.get('APP_ID', None)
    APP_SECRET = FACEBOOK.get('APP_SECRET', None)
    APP_ACCESS_TOKEN = FACEBOOK.get('APP_ACCESS_TOKEN', None)
    SCOPE = ','.join(FACEBOOK.get('SCOPE', ['email']))

    if not APP_ID:
        raise ImproperlyConfigured('A proper "APP_ID" must be specified '
            'in order to use socialnetwork.facebook module.')

    if not APP_SECRET:
        raise ImproperlyConfigured('A proper "APP_SECRET" must be specified '
            'in order to use socialnetwork.facebook module.')
