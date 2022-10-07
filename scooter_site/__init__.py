import os

if os.environ.get("ENV_NAME") == 'Production':
    from scooter_site.settings.prod.settings import *
else:
    from scooter_site.settings.dev.settings import *