from distutils.core import setup

setup(
    name            = 'mobileserverstatus',
    version         = '1.0',
    description     = 'MSS lets mobile devices to check that server is running and that app mobile version up to date.',
    author          = 'CIRB',
    author_email    = 'django@cirb.irisnet.be',
    url             = 'http://stash.cirb.lan/plugins/servlet/readmeparser/DJANGO/mobileserverstatus',
    package_dir     = {'mobileserverstatus': ''},
    packages        = ["mobileserverstatus"],
    classifiers     = [
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
    ],
)
