import json
from json.encoder import _make_iterencode


def max_stringify(s):
    while True:
        try:
            s = json.loads(s)
        except (json.decoder.JSONDecodeError, TypeError):
            break

    return json.dumps(s, ensure_ascii=False)


class MaxJSONEncoder(json.JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        if self.check_circular:
            markers = {}
        else:
            markers = None

        _iterencode = _make_iterencode(
            markers, self.default, max_stringify, self.indent, str,
            self.key_separator, self.item_separator, self.sort_keys,
            self.skipkeys, _one_shot)

        return _iterencode(o, 0)
