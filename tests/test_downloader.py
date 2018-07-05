import pytest
import requests_mock
from tests.fixtures import law_fixtures
from waffle import downloader


@pytest.fixture
def law_mocker() -> requests_mock.Mocker:
    with requests_mock.Mocker() as mocker:
        for fixture in law_fixtures.fixtures():
            mocker.get(str(fixture.url), text=fixture.content)
        yield mocker


@pytest.mark.usefixtures('law_mocker')
def test_downloader() -> None:
    download = downloader.Downloader()
    results = list(download.legislation('english'))
    assert len(results) == 3
    assert all([result.startswith('\n<!DOCTYPE html>\n') for result in results])
