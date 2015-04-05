print("Bootstrap from {}".format(__file__))

# Do an import * on the module version you would like to use
from {{ project_name }}.settings.dev import *

#EMAIL_HOST_PASSWORD = '...'

# Then, you are able to override or extend existing data structure.
# For example:
#DATABASES['default']['NAME'] = ''
#DATABASES['default']['USER'] = ''
#DATABASES['default']['PASSWORD'] = ''

# Any host overrides.
#ALLOWED_HOSTS += [ 'mysite.com' ]


