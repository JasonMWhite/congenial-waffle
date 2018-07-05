from pathlib import PurePath
from waffle.law_url import LawUrl


def test_from_string() -> None:
    output = LawUrl.from_string('/eng/acts/Z.html')
    assert str(output) == LawUrl.ROOT + "/eng/acts/Z.html"
    assert repr(output) == "LawUrl(PurePath(/eng/acts/Z.html))"


def test_from_string_on_index() -> None:
    output = LawUrl.from_string('/eng/acts/index.html')
    assert str(output) == LawUrl.ROOT + "/eng/acts/"
    assert repr(output) == "LawUrl(PurePath(/eng/acts/))"


def test_from_path() -> None:
    output = LawUrl(PurePath('/eng/acts/Z.html'))
    assert str(output) == LawUrl.ROOT + '/eng/acts/Z.html'
    assert repr(output) == "LawUrl(PurePath(/eng/acts/Z.html))"


def test_from_path_on_index() -> None:
    output = LawUrl(PurePath('/eng/acts/index.html'))
    assert str(output) == LawUrl.ROOT + '/eng/acts/'
    assert repr(output) == "LawUrl(PurePath(/eng/acts/))"


def test_from_path_no_root() -> None:
    output = LawUrl(PurePath('eng/acts/Z.html'))
    assert str(output) == LawUrl.ROOT + '/eng/acts/Z.html'
    assert repr(output) == "LawUrl(PurePath(/eng/acts/Z.html))"


def test_from_path_on_index_no_root() -> None:
    output = LawUrl(PurePath('eng/acts/index.html'))
    assert str(output) == LawUrl.ROOT + '/eng/acts/'
    assert repr(output) == "LawUrl(PurePath(/eng/acts/))"
