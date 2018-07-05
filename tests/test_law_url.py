from waffle.law_url import LawUrl


def test_file() -> None:
    output = LawUrl('/eng/acts/Z.html')
    assert str(output) == LawUrl.ROOT + '/eng/acts/Z.html'
    assert repr(output) == 'LawUrl(/eng/acts/Z.html)'


def test_file_no_root() -> None:
    output = LawUrl('eng/acts/Z.html')
    assert str(output) == LawUrl.ROOT + '/eng/acts/Z.html'
    assert repr(output) == 'LawUrl(/eng/acts/Z.html)'


def test_folder() -> None:
    output = LawUrl('/eng/acts/')
    assert str(output) == LawUrl.ROOT + '/eng/acts/'
    assert repr(output) == 'LawUrl(/eng/acts/)'


def test_index() -> None:
    output = LawUrl('/eng/acts/index.html')
    assert str(output) == LawUrl.ROOT + '/eng/acts/'
    assert repr(output) == 'LawUrl(/eng/acts/)'
