import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


# ---------- Starter examples ----------
def test_wet_soil_no_irrigation():
    assert should_irrigate(70, 0, "seedling") is False

def test_seedling_volume():
    assert water_volume(10, "seedling", 20) == 20


# ---------- should_irrigate ----------
def test_heavy_rain_no_irrigation():
    assert should_irrigate(30, 12, "vegetative") is False

def test_seedling_dry_irrigates():
    assert should_irrigate(40, 0, "seedling") is True

def test_flowering_dry_irrigates():
    assert should_irrigate(50, 0, "flowering") is True

def test_other_stage_light_rain_no_irrigation():
    assert should_irrigate(30, 6, "vegetative") is False

def test_other_stage_dry_irrigates():
    assert should_irrigate(30, 0, "vegetative") is True


# ---------- water_volume ----------
def test_invalid_area_raises():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)

def test_flowering_volume():
    assert water_volume(10, "flowering", 20) == 50

def test_default_stage_volume():
    assert water_volume(10, "vegetative", 20) == 40

def test_hot_weather_increases_volume():
    assert water_volume(10, "seedling", 40) == 30


# ---------- schedule ----------
def test_schedule_stops_when_budget_exceeded():
    zones = [
        ("A", 10, 30, 0, "vegetative", 20),   # needs 40 -> fits
        ("B", 10, 30, 0, "vegetative", 20),   # needs 40 -> exceeds remaining 10
    ]
    assert schedule(zones, 50) == ["A"]
