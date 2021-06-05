
# must be Debug = False but for static files i live it like this
# todo mode static data to s3
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dckh9bns3abpbh',
        'USER': 'srpkndhjrssvge',
        'PASSWORD': '4118c271e25ac5460a6f96e83e1454df2eb9d0b37d08858f1f57fc5be755fcfd',
        'HOST': 'ec2-52-209-134-160.eu-west-1.compute.amazonaws.com',
        'POST': '',
    }
}

print("Server running ================")