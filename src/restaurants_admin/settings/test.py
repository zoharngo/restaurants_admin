from base import *
import os

INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')

NOSE_ARGS = [
    '--verbosity=2'         # verbose output
    ,'--nologcapture'       # don't output log capture
    ,'--with-coverage'      # activate coverage report
    ,'--cover-package=api' # coverage reports will apply to these packages
    ,'--with-spec'          # spec style tests
    ,'--spec-color'
    ,'--with-xunit'         # enable xunit plugin
    ,'--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR  
    ,'--cover-xml'
    ,'--cover-xml-file=%s/coverage' % TEST_OUTPUT_DIR        
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'restaurants_admin'),
        'USER': os.environ.get('MYSQL_USER', 'api'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),        
    }
}