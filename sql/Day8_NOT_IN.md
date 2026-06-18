SQL DAY 8 - NOT IN

NOT IN is used to exclude multiple values.

Example:

SELECT * FROM students
WHERE city NOT IN ('Chennai','Mumbai');

Output:
Students from cities other than Chennai and Mumbai.

--------------------------------

IN

SELECT * FROM students
WHERE city IN ('Chennai','Mumbai');

Meaning:
Include Chennai and Mumbai.

--------------------------------

NOT IN

SELECT * FROM students
WHERE city NOT IN ('Chennai','Mumbai');

Meaning:
Exclude Chennai and Mumbai.

--------------------------------

Memory Trick

IN     -> Include values

NOT IN -> Exclude values
