import pytest
import requests_mock
from tests.fixtures import law_fixtures
from waffle import downloader


@pytest.fixture
def law_downloader() -> downloader.Downloader:
    with requests_mock.Mocker() as mocker:
        for fixture in law_fixtures.fixtures():
            mocker.get(str(fixture.url), text=fixture.content)
        yield downloader.Downloader()


def test_downloader(law_downloader: downloader.Downloader) -> None:
    results = list(law_downloader.legislation('english'))
    assert len(results) == 3
    assert all([result.startswith('\n<!DOCTYPE html>\n') for result in results])
