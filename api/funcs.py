from django.utils.translation import ugettext_lazy as _


class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None))


tasks = {
    1: Task(id=1, name='Demo', owner='gitter', status='Done'),
    2: Task(id=2, name='Model less demo', owner='gitter', status='Ongoing')
}


STATUS = (
    ('New', _('New')),
    ('Ongoing', _('Ongoing')),
    ('Done', _('Done'))
)
