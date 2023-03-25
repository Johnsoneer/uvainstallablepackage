import sys
sys.path.append('.')
import shared.shared as sh
from lab_2.test_shared import space_compress
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_newline_string():
    test_str = '''
    this is a string
    with several lines'''

    assert "this is a string with several lines" == space_compress(test_str), "String <{}> not cleaned as expected".format(test_str)

@pytest.mark.xfail
def test_fail_string():
    test_string = " This! is      a ,test string  "
    assert not "This is a test string" == space_compress(test_string),  "String <{}> not cleaned as expected".format(test_string)

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip_string():
    test_string = " This! is      a ,test string  "
    assert not "This is a test string" == space_compress(test_string), "String <{}> not cleaned as expected".format(test_string)

@pytest.mark.skipif(sys.platform == "darwin", reason='Skipped when run on the sys.platform=="darwin"')
def test_skip_again():
    print("My platform is", sys.platform)
    test_string = " This! is      a ,test string  "
    assert "This! is a test string" == space_compress(test_string), "String <{}> not cleaned as expected".format(test_string)

@pytest.mark.skipif(sys.platform != "darwin", reason='Skipped when NOT run on the sys.platform=="darwin"')
def test_skip_darwin():
    # this test should fail but only run when using "darwin" platform.
    print("My platform is", sys.platform)
    test_string = " This! is      a ,test string  "
    assert "This is a test string" == space_compress(test_string), "String <{}> not cleaned as expected".format(test_string)

