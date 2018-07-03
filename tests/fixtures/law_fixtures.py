from pathlib import Path
import typing
from waffle.config import PROJECT_ROOT

FIXTURES_ROOT = PROJECT_ROOT / 'tests' / 'fixtures'


def fixtures() -> typing.Iterable[typing.Tuple[Path, str]]:
    for fixture in FIXTURES_ROOT.glob('**/*.html'):
        relative = fixture.relative_to(FIXTURES_ROOT)
        contents = fixture.read_text()
        yield relative, contents
