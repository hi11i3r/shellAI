#test_run_python_file

from functions.run_python_file import run_python_file

print("\nResult for calculator, main.py:")
print(f'{run_python_file("calculator", "main.py")}')

print("\nResult for calculator, main.py, [3 + 5]:")
print(f'{run_python_file("calculator", "main.py", ["3 + 5"])}')

print("\nResult for calculator, tests.py")
print(f'{run_python_file("calculator", "tests.py")}\n')

print("\nResult for calculator, main.py:")
print(f'{run_python_file("calculator", "../main.py")}')

print("\nResult for calculator, nonexistent.py")
print(f'{run_python_file("calculator", "nonexistent.py")}')

print("\nResult for calculator, lorem.txt")
print(f'{run_python_file("calculator", "lorem.txt")}\n')
