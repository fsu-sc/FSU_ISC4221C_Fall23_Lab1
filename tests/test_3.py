import pytest
from answers_lab import cities_distances

def test_cities_distances():
    # Test with Tallahassee
    current_pos = (25.7753, 80.2089)
    cities, distances = cities_distances(*current_pos)
    assert [x.strip() for x in cities] == ['Miami','Hialeah','Orlando', 'Tampa','Gainesville','Jacksonville','Tallahassee']
    true_distances = [0.0, 12.74, 312.80, 331.70, 478.73, 526.85, 654.16]
    for i, d in enumerate(distances):
        assert d == pytest.approx(true_distances[i], 0.01)

    # Test with a random lat lon close to Tallahassee
    current_pos = (30.4, 83.8)
    cities, distances = cities_distances(*current_pos)
    assert [x.strip() for x in cities] == ['Tallahassee','Gainesville','Jacksonville',
                                           'Tampa','Orlando','Hialeah','Miami']
    true_distances = [ 43.89 ,164.56 ,205.29 ,299.38 ,327.66 ,610.62 ,623.23]
    for i, d in enumerate(distances):
        assert d == pytest.approx(true_distances[i], 0.01)