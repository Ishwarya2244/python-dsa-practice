SQL DAY 6 - LIKE

LIKE is used to search for patterns in text.

Starts With:

SELECT * FROM students
WHERE name LIKE 'I%';

Output:
Ishu
Indhu

--------------------------------

Ends With:

SELECT * FROM students
WHERE name LIKE '%a';

Output:
Priya

--------------------------------

Contains:

SELECT * FROM students
WHERE name LIKE '%am%';

Output:
Ram

--------------------------------

Memory Trick

I%   -> Starts with I

%a   -> Ends with a

%am% -> Contains am
