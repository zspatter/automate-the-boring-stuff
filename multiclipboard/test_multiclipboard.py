import shelve
import sys

import pyperclip
import pytest

from multiclipboard import mcb

shelf = shelve.open('test')
shelf.clear()
assert len(shelf) == 0


def entry_setup():
    pyperclip.copy('test1 text replaced')
    mcb.save_entry(shelf, 'test1')
    pyperclip.copy('test2 text')
    mcb.save_entry(shelf, 'test2')


@pytest.mark.skipif(sys.platform == 'linux',
                    reason="Pyperclip requires a copy/paste mechanism. "
                           "Cannot get any of these mechanisms to function "
                           "on Travis' linux vm. Only disabled for CI",
                    allow_module_level=True)
def test_save_entry():
    pyperclip.copy('test1 text')
    mcb.save_entry(shelf, 'test1')
    assert len(shelf) == 1

    pyperclip.copy('test2 text')
    mcb.save_entry(shelf, 'test2')
    assert len(shelf) == 2

    pyperclip.copy('test1 text replaced')
    mcb.save_entry(shelf, 'test1')
    assert len(shelf) == 2

    shelf.clear()


@pytest.mark.skipif(sys.platform == 'linux',
                    reason="Pyperclip requires a copy/paste mechanism. "
                           "Cannot get any of these mechanisms to function "
                           "on Travis' linux vm. Only disabled for CI",
                    allow_module_level=True)
def test_list_entries():
    entry_setup()

    mcb.list_entries(shelf)
    entries = pyperclip.paste()
    assert 'test1' in entries
    assert 'test2' in entries

    shelf.clear()


@pytest.mark.skipif(sys.platform == 'linux',
                    reason="Pyperclip requires a copy/paste mechanism. "
                           "Cannot get any of these mechanisms to function "
                           "on Travis' linux vm. Only disabled for CI",
                    allow_module_level=True)
def test_get_entry():
    entry_setup()

    mcb.get_entry(shelf, 'test1')
    assert 'test1 text replaced' == pyperclip.paste()

    shelf.clear()


@pytest.mark.skipif(sys.platform == 'linux',
                    reason="Pyperclip requires a copy/paste mechanism. "
                           "Cannot get any of these mechanisms to function "
                           "on Travis' linux vm. Only disabled for CI",
                    allow_module_level=True)
def test_delete_entry():
    entry_setup()

    assert len(shelf) == 2
    mcb.delete_entry(shelf, 'test2')
    assert len(shelf) == 1

    mcb.delete_entry(shelf, 'junk')
    assert pyperclip.paste() == 'Error: deletion failed as there is no ' \
                                'saved entry that matches "junk"'
    assert len(shelf) == 1

    shelf.clear()


@pytest.mark.skipif(sys.platform == 'linux',
                    reason="Pyperclip requires a copy/paste mechanism. "
                           "Cannot get any of these mechanisms to function "
                           "on Travis' linux vm. Only disabled for CI",
                    allow_module_level=True)
def test_delete_all_entries():
    pyperclip.copy('test1 text')
    mcb.save_entry(shelf, 'test1')
    assert len(shelf) == 1
    mcb.save_entry(shelf, 'test2')
    assert len(shelf) == 2

    mcb.delete_all_entries(shelf)
    assert len(shelf) == 0

    shelf.clear()
