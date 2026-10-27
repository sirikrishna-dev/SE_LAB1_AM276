# Lab 5: Static Code Analysis

## Objective

The objective of this lab is to analyze a Python program using three static code analysis tools: Pylint, Bandit, and Flake8. The issues identified by these tools were reviewed and fixes were applied to improve code quality, security, and coding-style compliance.

## Tools Used

- **Pylint:** Identifies code quality issues, naming convention violations, and missing documentation.
- **Bandit:** Identifies common security-related issues in Python code.
- **Flake8:** Checks Python code for style violations and linting issues.

## Files in This Repository

| File | Description |
|---|---|
| `todo_manager.py` | Python task manager after applying fixes. |
| `pylint_report_before.txt` | Pylint analysis report before fixing issues. |
| `pylint_report_after.txt` | Pylint analysis report after fixing issues. |
| `bandit_report_before.txt` | Bandit security analysis report before fixing issues. |
| `bandit_report_after.txt` | Bandit security analysis report after fixing issues. |
| `flake8_report_before.txt` | Flake8 analysis report before fixing issues. |
| `flake8_report_after.txt` | Flake8 analysis report after fixing issues. |

## Issues Addressed

The following improvements were made to the program:

- Added a module-level docstring.
- Removed unused imports.
- Replaced the mutable default argument with `None`.
- Replaced pickle-based persistence with JSON serialization.
- Removed the unused email-reminder helper that invoked an external command.
- Replaced random task selection with priority-based task selection.
- Added handling for an empty pending-task list.
- Improved function naming and code formatting.

## Running the Program

Ensure Python 3 is installed, then run:

```bash
python todo_manager.py
```

## Running the Analysis Tools

Install the tools:

```bash
pip install pylint bandit flake8
```

Run Pylint:

```bash
pylint todo_manager.py
```

Run Bandit:

```bash
bandit todo_manager.py
```

Run Flake8:

```bash
flake8 todo_manager.py
```

## Results

The before-and-after reports are included in this repository to demonstrate the analysis results and the effect of the code fixes.

- **Pylint:** The latest uploaded report shows a score of 10.00/10.
- **Bandit:** The latest uploaded report reports no issues identified.
- **Flake8:** Refer to the final after-analysis report to verify that all reported style violations have been resolved.

## Git Commits

Three separate commits are required to document the fixes associated with the three analysis tools:

1. Pylint-related code quality fixes.
2. Bandit-related security fixes.
3. Flake8-related style fixes.

## Conclusion

This lab demonstrates how static analysis tools can identify different categories of issues in Python programs. Applying the fixes and comparing the before-and-after reports helps improve code quality, security awareness, and coding consistency.
