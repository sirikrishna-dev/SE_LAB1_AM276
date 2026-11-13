# Irrigation Scheduler – Lab 7: Fuzz Testing

## 1. Project Overview

This project focuses on identifying and fixing input validation bugs in a Python-based Irrigation Scheduler application using **Fuzz Testing** and the **Hypothesis** property-based testing library.

The application accepts user inputs related to irrigation zones, soil moisture readings, and water requirements. Hypothesis is used to generate unexpected and malformed inputs to identify potential runtime errors and improve application robustness.

## 2. Functions Tested

The application contains three main functions:

| Function                         | Description                                                                |
| -------------------------------- | -------------------------------------------------------------------------- |
| `parse_zone(text)`               | Parses the irrigation zone name and its area from a colon-separated input. |
| `moisture_average(readings_csv)` | Calculates the integer average of comma-separated soil moisture readings.  |
| `water_needed(text)`             | Calculates the water required based on plot area and rainfall.             |

## 3. Technologies Used

- Python 3
- Hypothesis – Property-based fuzz testing
- Pytest – Test execution framework
- Google Colab – Development and execution environment

## 4. Repository Structure

```text
── lab7/
    ├── irrigation_scheduler.py
    ├── test_irrigation_scheduler.py
    └── README.md
```

## 5. Installation and Setup

Install the required dependencies:

```bash
pip install hypothesis pytest
```

Navigate to the Lab 7 directory:

```bash
cd lab7
```

## 6. Running the Application

Execute the original or fixed application using:

```bash
python irrigation_scheduler.py
```

The application accepts three inputs:

1. Zone name and area (e.g., `north:120`)
2. Soil moisture readings (e.g., `40,35,50`)
3. Plot area and rainfall (e.g., `120|8`)

## 7. Fuzz Testing Using Hypothesis

Hypothesis was used to automatically generate unexpected inputs for all three functions.

The following strategy was used:

```python
@given(st.text() | st.none())
```

This generates random Unicode strings and `None` values to test how the functions handle unexpected inputs.

The tests were designed to identify:

- Empty inputs
- Missing separators
- Malformed input formats
- Invalid numerical values
- None inputs
- Unexpected strings

## 8. Bugs Identified

Fuzz testing identified the following issues in the original implementation:

### parse_zone()

- Failed when the input was empty.
- Failed when the area value was missing.
- Raised an AttributeError when given None.

### moisture_average()

- Failed when the input was empty.
- Raised an AttributeError when given None.
- Could not handle malformed numerical readings.

### water_needed()

- Failed when the separator or numerical values were missing.
- Raised an AttributeError when given None.
- Could not handle malformed numerical inputs.

## 9. Bug Fixes and Improvements

The application was modified using defensive programming and input validation.

The improvements include:

- Checking input types before processing.
- Validating the number of input components.
- Rejecting empty fields.
- Handling invalid numerical conversions.
- Rejecting negative and non-finite values where applicable.
- Returning `None` for invalid inputs instead of allowing runtime exceptions.

Valid input calculations retain the original functionality.

## 10. Running the Tests

Execute the test suite using:

```bash
pytest -v test_irrigation_scheduler.py
```

Alternatively:

```bash
python -m pytest -v test_irrigation_scheduler.py
```

## 11. Test Results

The final test suite contains seven tests:

- Three Hypothesis-based tests covering the three application functions.
- Three tests checking valid input behaviour.
- One test checking invalid input behaviour.

**Final Result: 7 tests passed.**

The tests were executed successfully in Google Colab.

## 12. Sample Output

For the following inputs:

```text
Zone: north:120
Moisture readings: 40,35,50
Plot area and rainfall: 120|8
```

Expected output:

```text
Zone and Area: ('North', 120.0)
Average Moisture: 41
Water Needed: 592.0
```

## 13. Deliverables

The following files are included in the submission:

1. `irrigation_scheduler.py` – Fixed application with input validation.
2. `test_irrigation_scheduler.py` – Updated Hypothesis fuzz tests.
3. `Lab7_Screenshots.pdf` – Screenshots documenting original execution, discovered failures, fixed execution, and passing tests.

## 14. Conclusion

This lab demonstrates how property-based fuzz testing can identify input validation bugs that may not be detected through ordinary testing.

Using Hypothesis and Pytest, unexpected inputs were automatically generated, failures were identified, and the application was improved through defensive programming.

The final implementation successfully passed all seven tests, demonstrating improved robustness against the tested edge cases.

