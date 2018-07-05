from pathlib import PurePath


class LawUrl:
    ROOT = "http://laws-lois.justice.gc.ca"

    def __init__(self, path: PurePath) -> None:
        path = path if path.root == '/' else PurePath('/').joinpath(path)
        self.path = path

    @classmethod
    def from_string(cls, path: str) -> 'LawUrl':
        return LawUrl(PurePath(path))

    def _normalize_parts(self) -> str:
        parts = list(self.path.parts)
        parts = parts[1:] if parts[0] == '/' else parts
        if parts[-1] == 'index.html':
            parts[-1] = ''
        return '/'.join(parts)

    def __str__(self) -> str:
        return '/'.join([self.ROOT, self._normalize_parts()])

    def __repr__(self) -> str:
        return f"LawUrl(PurePath(/{self._normalize_parts()}))"
