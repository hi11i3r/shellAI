#test_get_file_content

from functions.get_file_content import get_file_content

print("\nResult for calculator/lorem.txt:")
print(f'{get_file_content("calculator", "lorem.txt")}')
print("\nResult for calculator/main.py:")
print(f'{get_file_content("calculator", "main.py")}')
print("\nResult for calculator/pkg/calculator.py:")
print(f'{get_file_content("calculator", "pkg/calculator.py")}')
print("\nResult for calculator/bin/cat:")
print(f'{get_file_content("calculator", "/bin/cat")}')
print("\nResult for calculator/pkg/does_not_exist.py:")
print(f'{get_file_content("calculator", "/pkg/does_not_exist.py")}')