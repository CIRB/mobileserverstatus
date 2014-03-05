# Mobile Server Status

MSS lets mobile devices to check that server is running and that app mobile version up to date.

## Install

* Add mobileserverstatus to INSTALLED_APPS:

    INSTALLED_APPS = (
        [..]
        'mobileserverstatus',
        [..]
    )

* Add the application to urls:

    (r'^status/', include('mobileserverstatus.urls')),

* Add one message to django /admin/mobileserverstatus/message/.

That's all.
