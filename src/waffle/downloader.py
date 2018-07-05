import typing
from lxml import html
import requests
from dataclasses import dataclass
from waffle.logger import LOG
from waffle.law_url import LawUrl


@dataclass
class _DownloadResults:
    path: LawUrl
    links: typing.List[LawUrl]
    content: str


class Downloader:
    LAWS = {
        'english': "eng/acts/",
        'french': "fra/lois/",
    }

    def legislation(self, language: str) -> typing.Iterable[str]:
        location = LawUrl(self.LAWS[language])
        yield from self._fetch_pages([location])

    def _fetch_pages(self, paths: typing.List[LawUrl]) -> typing.Iterable[str]:
        for path in paths:
            LOG.debug("Fetching page at %s", path)
            results = self._process_page(path)
            if results.content:
                yield results.content
            yield from self._fetch_pages(results.links)

    @staticmethod
    def _process_page(location: LawUrl) -> _DownloadResults:
        LOG.debug("Processing page at %s", location)
        resp = requests.get(str(location))
        body = resp.content.decode("UTF-8")

        if str(location).endswith('.html'):
            paths = []
        else:
            root = html.fromstring(body)
            letters = root.findall('.//div[@id="alphaList"]//a')
            paths = [resp.request.path + letter.attrib['href'] for letter in letters if letter.attrib['href'] != '#']
        links = [LawUrl(path) for path in paths]
        return _DownloadResults(path=location, links=links, content=body)
