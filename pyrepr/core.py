import json
from io import StringIO
from prettyprinter import pprint, cpprint

from .util import MaxJSONEncoder


class Repr:
    def __init__(self, obj):
        self.obj = json.loads(json.dumps(obj, cls=MaxJSONEncoder))
        self.str_io = StringIO()

        pprint(self.obj, self.str_io)

    def __str__(self):
        return self.str_io.getvalue()

    def __repr__(self):
        return str(self)

    @property
    def html(self):
        return str(self).replace('\n', '<br/>').replace(' ', '&nbsp;')

    def _repr_html_(self):
        cpprint(self.obj)
        return ''
