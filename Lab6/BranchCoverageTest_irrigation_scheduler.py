import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


# ================= should_irrigate =================
def test_wet_soil_no_irrigation():
    assert should_irrigate(70, 0, "seedling") is False

def test_moisture_boundary_60_no_irrigation():
    assert should_irrigate(60, 0, "vegetative") is False

def test_heavy_rain_no_irrigation():
    assert should_irrigate(30, 12, "vegetative") is False

def test_rain_boundary_10_no_irrigation():
    assert should_irrigate(30, 10, "vegetative") is False

def test_seedling_dry_irrigates():
    assert should_irrigate(40, 0, "seedling") is True

def test_seedling_moderate_moisture_no_irrigation():
    assert should_irrigate(50, 0, "seedling") is False

def test_seedling_boundary_45_no_irrigation():
    assert should_irrigate(45, 0, "seedling") is False

def test_flowering_dry_irrigates():
    assert should_irrigate(50, 0, "flowering") is True

def test_flowering_moist_no_irrigation():
    assert should_irrigate(55, 0, "flowering") is False

def test_other_stage_light_rain_no_irrigation():
    assert should_irrigate(30, 6, "vegetative") is False

def test_rain_boundary_5_no_irrigation():
    assert should_irrigate(30, 5, "vegetative") is False

def test_other_stage_dry_irrigates():
    assert should_irrigate(30, 0, "vegetative") is True

def test_other_stage_moisture_boundary_40_no_irrigation():
    assert should_irrigate(40, 0, "vegetative") is False


# ================= water_volume =================
def test_invalid_area_zero_raises():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)

def test_invalid_area_negative_raises():
    with pytest.raises(ValueError):
        water_volume(-5, "flowering", 20)

def test_seedling_volume():
    assert water_volume(10, "seedling", 20) == 20

def test_flowering_volume():
    assert water_volume(10, "flowering", 20) == 50

def test_default_stage_volume():
    assert water_volume(10, "vegetative", 20) == 40

def test_hot_weather_increases_volume():
    assert water_volume(10, "seedling", 40) == 30

def test_temp_boundary_35_not_hot():
    assert water_volume(10, "seedling", 35) == 20

def test_cold_weather_decreases_volume():
    assert water_volume(10, "seedling", 5) == 10

def test_temp_boundary_10_not_cold():
    assert water_volume(10, "seedling", 10) == 20


# ================= schedule =================
def test_schedule_empty_zones():
    assert schedule([], 100) == []

def test_schedule_skips_zone_that_needs_no_water():
    zones = [("Wet", 10, 80, 0, "vegetative", 20)]
    assert schedule(zones, 100) == []

def test_schedule_waters_all_zones_within_budget():
    zones = [
        ("A", 10, 30, 0, "vegetative", 20),   # 40
        ("B", 5, 30, 0, "flowering", 20),     # 25
    ]
    assert schedule(zones, 100) == ["A", "B"]

def test_schedule_stops_when_budget_exceeded():
    zones = [
        ("A", 10, 30, 0, "vegetative", 20),   # 40 -> fits
        ("B", 10, 30, 0, "vegetative", 20),   # 40 -> exceeds remaining 10
    ]
    assert schedule(zones, 50) == ["A"]

def test_schedule_skip_then_water():
    zones = [
        ("Wet", 10, 80, 0, "vegetative", 20),  # skipped
        ("Dry", 10, 30, 0, "vegetative", 20),  # 40 -> fits
    ]
    assert schedule(zones, 40) == ["Dry"]

def test_schedule_exact_budget_is_allowed():
    zones = [("A", 10, 30, 0, "vegetative", 20)]   # needs exactly 40
    assert schedule(zones, 40) == ["A"]
