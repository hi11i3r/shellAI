from functions.get_files_info import get_files_info

print("\nResult for current directory:")
print(f'{get_files_info("calculator", ".")}\n')
print("\nResult for 'pkg' directory:")
print(f'{get_files_info("calculator", "pkg")}\n')
print("\nResult for '/bin' directory:")
print(f'{get_files_info("calculator", "/bin")}\n')
print("\nResult for '../' directory:")
print(f'{get_files_info("calculator", "../")}\n')