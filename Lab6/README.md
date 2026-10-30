# Lab 6: Code and Branch Coverage Analysis

**Project:** L6_L7_37 Irrigation Scheduler
**Name:** Siri Krishna CR  |  **SRN:** PES1UG24AM276

## About the application
`irrigation_scheduler.py` decides when a field zone needs watering, how much water it needs, and builds a watering schedule within a water budget. It has three functions:

| Function | Purpose |
|----------|---------|
| `should_irrigate(moisture, rain_mm, stage)` | Decides whether a zone should be watered, based on soil moisture, rainfall and growth stage |
| `water_volume(area_m2, stage, temp_c)` | Calculates litres needed; raises `ValueError` for an invalid area |
| `schedule(zones, budget)` | Waters zones in order until the water budget runs out |

## Files
| File | Description |
|------|-------------|
| `irrigation_scheduler.py` | Application code under test |
| `test_irrigation_scheduler.py` | Starter test file |
| `CodeCoverageTest_irrigation_scheduler.py` | Test cases for code (line) coverage, 12 tests |
| `BranchCoverageTest_irrigation_scheduler.py` | Test cases for branch coverage, 28 tests |
| `code coverage.png` | Terminal screenshot of the line coverage run |
| `branch coverage.png` | Terminal screenshot of the branch coverage run |

## How to run
```bash
pip install coverage pytest

# Code (line) coverage
coverage run -m pytest CodeCoverageTest_irrigation_scheduler.py
coverage report -m

# Branch coverage
coverage erase
coverage run --branch -m pytest BranchCoverageTest_irrigation_scheduler.py
coverage report -m
```

## Results
| Run | Tests | Result | Coverage |
|-----|-------|--------|----------|
| Code coverage | 12 passed | 3 of 38 statements missed (lines 9, 29, 37) | **92%** |
  | Branch coverage | 28 passed | 0 statements missed, 28 of 28 branches covered | **100%** |Pngs both line and branch coverage to 100%.
- Line coverage only checks whether each line ran at least once. Branch coverage checks that each decision went both ways. This is why the branch tests had to include extra cases such as zero or negative area, an empty zone list, and an exact-budget match.

## Commits
1. Add code coverage tests (>=90% line coverage)
2. Add branch coverage tests (>=90% branch coverage)
