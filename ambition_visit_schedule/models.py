from django.conf import settings

if settings.APP_NAME == 'ambition_visit_schedule':
    from .tests.models import TestModel
