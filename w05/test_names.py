from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Drew','LaMunyon') == 'LaMunyon; Drew'

def test_extract_family_name():
    assert extract_family_name('LaMunyon; Drew') == 'LaMunyon'
    
def test_extract_given_name():
    assert extract_given_name('LaMunyon; Drew') == 'Drew'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])