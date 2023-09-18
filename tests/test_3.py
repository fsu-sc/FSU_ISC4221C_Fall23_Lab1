import pytest
from answers_lab import cities_distances

def test_cities_distances():
    # Test with a city that exists in the file
    city = "Miami"
    cities, distances = cities_distances(city)
    assert [x.strip() for x in cities] == ['Hialeah','Orlando', 'Tampa','Gainesville','Jacksonville','Tallahassee']
    true_distances = [12.74, 312.80, 331.70, 478.73, 526.85, 654.16]
    for i, d in enumerate(distances):
        assert d == pytest.approx(true_distances[i], 0.01)

    # Test with a city that exists in the file
    city = "Orlando"
    cities, distances = cities_distances(city)
    assert [x.strip() for x in cities] == ['Tampa','Gainesville','Jacksonville','Hialeah','Miami','Tallahassee']
    true_distances = [ 125.68 ,169.84 ,216.48 ,301.02 ,312.80 ,365.04]
    for i, d in enumerate(distances):
        assert d == pytest.approx(true_distances[i], 0.01)

    city = "Chicago"
    with pytest.raises(Exception):
        cities_distances(city)
