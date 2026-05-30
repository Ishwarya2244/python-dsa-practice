Part 1 — What is File Handling?

File handling means:

reading from files or writing data into files using Python.

Example:

saving student marks,
storing usernames,
reading reports,
loading datasets.
Part 2 — Opening a File
Syntax
file = open("sample.txt", "r")
Here:
"sample.txt" → filename
"r" → read mode
Part 3 — Read Mode (r)

Used to read file content.

Example

Suppose sample.txt contains:

Hello Ishu

Python code:

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
Output
Hello Ishu
Part 4 — Write Mode (w)

Used to write data into file.

⚠ Important:
w mode replaces old content.

Example
file = open("sample.txt", "w")

file.write("Welcome Ishu")

file.close()

Now file content becomes:

Welcome Ishu
Part 5 — Append Mode (a)

Used to add new content without deleting old content.

Example
file = open("sample.txt", "a")

file.write("\nPython Learning")

file.close()
File content becomes:
Welcome Ishu
Python Learning

Part 6 — Why close() is Important?
file.close()
It:
saves changes properly,
frees memory,
closes file safely.   """"file.close() is used to close the file properly, save changes, and free system resources."""
