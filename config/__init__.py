""" Stores configuration information.
"""

import os


DJANGO = {
    'secret_key': load_config_key('EUPRIME_DJANGO_SECRET_KEY'),
}

TOOLKIT = {
    'username': load_config_key('EUPRIME_TOOLKIT_USERNAME'),
    'password': load_config_key('EUPRIME_TOOLKIT_PASSWORD'),
    'db_name': load_config_key('EUPRIME_TOOLKIT_DB_NAME'),
    'db_user': load_config_key('EUPRIME_TOOLKIT_DB_USERNAME'),
    'db_pass': load_config_key('EUPRIME_TOOLKIT_DB_PASSWORD'),
}

def load_config_key(key):
    """ Loads a configuration key from an environment variable

    Args:
        key: String containing the environment variable to load
    Raises:
        Exception: If environment variable not set

    """
    if not key in os.environ:
        raise Exception('Configuration environment variable not set: %s' % key)
    return os.environ[key]
