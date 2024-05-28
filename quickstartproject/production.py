from .settings import *
import os

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
CUSTOM_HOSTNAME='www.mohankopalle.in'
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else [CUSTOM_HOSTNAME]
# ALLOWED_HOSTS = ['www.mohankopalle.in']

DEBUG = False
