# python_basics_lecture8
# Student Utilities

## Description
This Python module contains utility functions for calculating a student's average marks, checking pass status, and assigning grades based on the average.

## Functions

### 1. `calculate_average(marks)`
Calculates the average of the marks provided in a list.

- **Parameter:** `marks` — a list of marks.
- **Returns:** The average of the marks.

**Example:**
```python
calculate_average([80, 90, 100])
# Output: 90.0
```

### 2. `is_passing(mark)`
Checks whether a student has passed.

- **Parameter:** `mark` — the student's marks.
- **Returns:** `True` if marks are 40 or above; otherwise, `False`.

**Example:**
```python
is_passing(40)
# Output: True
```

### 3. `get_grade(average)`
Assigns a grade based on the student's average marks.

| Average Marks | Grade |
|---|---|
| 90 and above | Distinction |
| 60–89 | First |
| 45–59 | Second |
| Below 45 | Fail |

**Example:**
```python
get_grade(95)
# Output: "Distinction"
```

## Constant

- `PASS_MARK = 40` — defines the minimum marks required to pass.

## How to Run

1. Save the code in `student_utils.py`.
2. Run the file using Python:

```bash
python student_utils.py
```

**Expected Output:**
```text
90.0
```

## Concepts Used
- Python functions
- Variables and constants
- Loops
- Conditional statements
- Lists
- Return statements
