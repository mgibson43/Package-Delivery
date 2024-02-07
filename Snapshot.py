import copy


class Snapshot:
    def __init__(self, time, pkg_list):
        self.time = time
        self.pkg_list = copy.deepcopy(pkg_list)
