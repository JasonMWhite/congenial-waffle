from dataclasses import dataclass
from waffle.law_url import LawUrl
import typing
from waffle.config import PROJECT_ROOT

FIXTURES_ROOT = PROJECT_ROOT / 'tests' / 'fixtures'


@dataclass
class LawFixture:
    url: LawUrl
    content: str


def fixtures() -> typing.Iterable[LawFixture]:
    for fixture in FIXTURES_ROOT.glob('**/*.html'):
        relative = fixture.relative_to(FIXTURES_ROOT)
        content = fixture.read_text()
        yield LawFixture(url=LawUrl(str(relative)), content=content)
