import typing
from lxml import html
import requests
from dataclasses import dataclass
from waffle.logger import LOG
from waffle.law_url import LawUrl


@dataclass
class _FollowResults:
    path: LawUrl
    links: typing.List[LawUrl]


@dataclass
class DownloadResults:
    path: LawUrl
    content: str


class Downloader:
    LAWS = {
        'english': "eng/acts/",
        'french': "fra/lois/",
    }

    def legislation(self, language: str) -> typing.Iterable[DownloadResults]:
        location = LawUrl(self.LAWS[language])
        yield from self._fetch_pages([location])

    def _fetch_pages(self, paths: typing.List[LawUrl]) -> typing.Iterable[DownloadResults]:
        for path in paths:
            LOG.debug("Fetching page at %s", path)
            follow, downloaded = self._process_page(path)

            if downloaded:
                yield downloaded
            yield from self._fetch_pages(follow.links)

    @staticmethod
    def _process_page(location: LawUrl) -> typing.Tuple[_FollowResults, typing.Optional[DownloadResults]]:
        LOG.debug("Processing page at %s", location)
        resp = requests.get(str(location))
        body = resp.content.decode("UTF-8")

        download: typing.Optional[DownloadResults] = None
        if str(location).endswith('.html'):
            paths = []
            download = DownloadResults(path=location, content=body)
        else:
            root = html.fromstring(body)
            letters = root.findall('.//div[@id="alphaList"]//a')
            paths = [resp.request.path + letter.attrib['href'] for letter in letters if letter.attrib['href'] != '#']

        links = [LawUrl(path) for path in paths]
        return _FollowResults(path=location, links=links), download
