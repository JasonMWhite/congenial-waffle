class LawUrl:
    ROOT = "http://laws-lois.justice.gc.ca"

    def __init__(self, path: str) -> None:
        parts = path.split('/')
        parts = parts[1:] if parts[0] == '' else parts
        if parts[-1] == 'index.html':
            parts[-1] = ''
        self._parts = parts

    def path(self) -> str:
        return '/' + '/'.join(self._parts)

    def __str__(self) -> str:
        return self.ROOT + self.path()

    def __repr__(self) -> str:
        return f"LawUrl({self.path()})"
