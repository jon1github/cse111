from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city('number street, city, state zipcode') == 'city'
    
def test_extract_state():
    assert extract_state('number street, city, state zipcode') == 'state'

def test_extract_zipcode():
    assert extract_zipcode('number street, city, state zipcode') == 'zipcode'
    
pytest.main(["-v", "--tb=line", "-rN", __file__])