# Code Audit: Student Utilities

## 1. Overview
The `student_utils.py` file contains three functions:
- `calculate_average(marks)` — calculates average marks.
- `is_passing(mark)` — checks whether a student has passed.
- `get_grade(average)` — assigns a grade based on average marks.

The original code contained **three logical errors**.

## 2. Errors Identified

### Error 1: Incorrect Average Calculation
**Incorrect code:**
```python
return total / (len(marks) - 1)
```

**Correct code:**
```python
return total / len(marks)
```

**Reason:** Subtracting 1 from the list length produces an incorrect average.

**Example:**
- Marks: `[80, 90, 100]`
- Incorrect average: `135.0`
- Correct average: `90.0`

### Error 2: Incorrect Passing Condition
**Incorrect code:**
```python
if mark > PASS_MARK:
```

**Correct code:**
```python
if mark >= PASS_MARK:
```

**Reason:** The original condition incorrectly treats 40 marks as a failure. Using `>=` ensures that a student scoring exactly 40 passes.

### Error 3: Incorrect Grade Conditions
**Incorrect code:**
```python
if average >= 60:
    return "First"

elif average >= 45:
    return "Second"

elif average >= 90:
    return "Distinction"
```

**Correct code:**
```python
if average >= 90:
    return "Distinction"

elif average >= 60:
    return "first"

elif average >= 45:
    return "second"
```

**Reason:** The original code checks `average >= 60` before `average >= 90`. Therefore, students scoring 90 or above incorrectly receive `"First"` instead of `"Distinction"`.

The conditions must be checked from highest to lowest.

## 3. Testing

| Test Case | Input | Expected Output |
|---|---|---|
| Average calculation | `[80, 90, 100]` | `90.0` |
| Passing marks | `40` | `True` |
| Failing marks | `35` | `False` |
| Distinction grade | `95` | `"Distinction"` |
| First grade | `75` | `"first"` |
| Second grade | `50` | `"second"` |
| Fail grade | `30` | `"Fail"` |

## 4. Conclusion
The audit identified and corrected three logical errors involving average calculation, passing criteria, and grade assignment.

The corrected code produces accurate results for the test cases listed above.

**Status:** All three identified errors corrected.
