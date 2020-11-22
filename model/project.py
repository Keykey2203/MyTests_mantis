from sys import maxsize

class Project:

    def __init__(self, id=None, name=None, status=None, inherit_global=None, view_state=None, desc=None, enabled=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.desc = desc
        self.id = id
        self.enabled = enabled

    def __repr__(self):
        return "%s;%s;%s;%s;%s" % (self.name, self.status, self.inherit_global, self.view_state, self.desc)

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def sort_by_name(self):
        if self.name:
            return self.name
        else:
            return "a"
