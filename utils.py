class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.lines = list()
        self._get_lines()

    def _get_lines(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.lines.append(line)

    def get_strings(self) -> list:
        if not self.lines:
            return []
        return self.lines[:]

    def get_ints(self) -> list:
        if not self.lines:
            return []
        return [int(n) for n in self.lines]

    def close(self):
        self.lines = []
        self.filename = ''

