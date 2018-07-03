from tests.fixtures import law_fixtures


def test_law_fixtures() -> None:
    all_fixtures = list(law_fixtures.fixtures())
    assert len([fixture for fixture, _ in all_fixtures if fixture.parts[0] == 'eng']) == 3
    assert len([fixture for fixture, _ in all_fixtures if fixture.parts[0] == 'fra']) == 3
