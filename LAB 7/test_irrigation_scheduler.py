from hypothesis import given, strategies as st

from irrigation_scheduler import parse_zone, moisture_average, water_needed


@given(st.text() | st.none())
def test_parse_zone_no_crash(value):
    result = parse_zone(value)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and isinstance(result[0], str)
        and isinstance(result[1], float)
    )


@given(st.text() | st.none())
def test_moisture_average_no_crash(value):
    result = moisture_average(value)
    assert result is None or isinstance(result, int)


@given(st.text() | st.none())
def test_water_needed_no_crash(value):
    result = water_needed(value)
    assert result is None or isinstance(result, float)


def test_valid_parse_zone():
    assert parse_zone("north:120") == ("North", 120.0)


def test_valid_moisture_average():
    assert moisture_average("40,35,50") == 41


def test_valid_water_needed():
    assert water_needed("120|8") == 592.0


def test_invalid_inputs():
    assert parse_zone(None) is None
    assert parse_zone(":") is None
    assert moisture_average("") is None
    assert moisture_average(None) is None
    assert water_needed("|") is None
    assert water_needed(None) is None
