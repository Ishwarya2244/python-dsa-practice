SQL DAY 7 - IN OPERATOR

IN is used to check multiple values.

Example:

SELECT * FROM students
WHERE city IN ('Chennai','Mumbai');

Output:
All students from Chennai and Mumbai.

--------------------------------

Without IN:

SELECT * FROM students
WHERE city = 'Chennai'
OR city = 'Mumbai';

--------------------------------

With IN:

SELECT * FROM students
WHERE city IN ('Chennai','Mumbai');

--------------------------------

Memory Trick:

=  -> One value

city = 'Chennai'

IN -> Multiple values

city IN ('Chennai','Mumbai')
