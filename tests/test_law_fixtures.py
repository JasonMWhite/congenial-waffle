from tests.fixtures import law_fixtures


def test_law_fixtures() -> None:
    all_fixtures = list(law_fixtures.fixtures())
    assert len(all_fixtures) == 6
    assert len([fixture for fixture in all_fixtures if fixture.url.path().startswith('/eng/acts')]) == 3
    assert len([fixture for fixture in all_fixtures if fixture.url.path().startswith('/fra/lois')]) == 3
    assert len([fixture for fixture in all_fixtures if fixture.url.path().endswith('/')]) == 2
