SQL DAY 9 - BETWEEN

BETWEEN is used to find values within a range.

Example:

SELECT * FROM students
WHERE marks BETWEEN 60 AND 80;

Output:
Values from 60 to 80.

--------------------------------

Important:

BETWEEN includes both starting and ending values.

BETWEEN 60 AND 80

Means:

60 <= value <= 80

--------------------------------

Example:

SELECT * FROM students
WHERE age BETWEEN 18 AND 25;
