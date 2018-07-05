from tests.fixtures import law_fixtures


def test_law_fixtures() -> None:
    all_fixtures = list(law_fixtures.fixtures())
    assert len(all_fixtures) == 6
    assert len([fixture for fixture in all_fixtures if str(fixture.url.path.parent) == '/eng/acts']) == 3
    assert len([fixture for fixture in all_fixtures if str(fixture.url.path.parent) == '/fra/lois']) == 3
    assert len([fixture for fixture in all_fixtures if str(fixture.url).endswith('/')]) == 2
